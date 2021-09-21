from django.shortcuts import redirect, render, reverse
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    """ A view to render the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
