from django.shortcuts import (
    get_object_or_404, redirect, render, reverse, HttpResponse
)
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

from games.models import Edition
from adoption.models import Package

from .models import Order, OrderLineItem, Product
from .forms import OrderForm
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """ Add saved info to payment intent in metadata key """

    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ A view to render the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'street_address': request.POST['street_address'],
            'street_address_2': request.POST['street_address_2'],
            'country': request.POST['country'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'phone_number': request.POST['phone_number'],
        }
        form = OrderForm(form_data)

        if form.is_valid():
            order = form.save()
            # Iterate through cart items to create each line item
            for product_type in cart.items():
                if 'game' in product_type:
                    for item in product_type:
                        if isinstance(item, dict):
                            for item_id, quantity in item.items():
                                try:
                                    game = Edition.objects.get(sku=item_id)
                                    try:
                                        product = Product.objects.get(
                                            sku=item_id)
                                    except Product.DoesNotExist:
                                        product = Product.objects.create(
                                            sku=item_id,
                                            game=game,
                                            price=game.price,
                                        )
                                    order_line_item = OrderLineItem(
                                        order=order,
                                        product=product,
                                        quantity=quantity,
                                    )
                                    order_line_item.save()

                                except Edition.DoesNotExist:
                                    messages.error(request, (
                                        "Cart item not found in our database. "
                                        "Please contact us for assistance!"
                                    ))
                                    order.delete()
                                    return redirect(reverse('view_cart'))
                elif 'adoption' in product_type:
                    for item in product_type:
                        if isinstance(item, dict):
                            for item_id, quantity in item.items():
                                try:
                                    adoption = Package.objects.get(sku=item_id)
                                    product = Product.objects.create(adoption=adoption, price=adoption.price)
                                    order_line_item = OrderLineItem(
                                        order=order,
                                        product=product,
                                        quantity=quantity,
                                    )
                                    order_line_item.save()

                                except Package.DoesNotExist:
                                    messages.error(request, (
                                        "Cart item not found in our database. "
                                        "Please contact us for assistance!"
                                    ))
                                    order.delete()
                                    return redirect(reverse('view_cart'))

            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your shopping cart!")
        return redirect(reverse('games'))

    current_cart = cart_contents(request)
    total = current_cart['total']

    stripe_total = round(total * 100)

    # Set secret key on stripe
    stripe.api_key = stripe_secret_key

    # Create Stripe payment intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    form = OrderForm()

    # Alert if public key is missing
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ A view to render successful checkouts """

    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request, f'Order Successfully Processed! \
            Your order number is {order_number}. \
            A confirmation email will be sent to {order.email}'
    )

    # Delete shopping cart from session
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
