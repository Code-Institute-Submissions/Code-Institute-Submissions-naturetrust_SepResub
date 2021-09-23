from adoption.models import Adoption, Package
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib import messages

from games.models import Edition


def view_cart(request):
    """ A view that renders the shopping cart contents """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add game and its quanitity
    to shopping cart """

    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')

    product_type = request.POST.get('product_type')

    if product_type == 'game':
        game_edition = get_object_or_404(Edition, sku=item_id)
    elif product_type == 'adoption':
        adoption_package = get_object_or_404(Package, sku=item_id)

    cart = request.session.get('cart', {})

    if cart:
        if product_type in cart:
            if item_id in cart[product_type]:
                cart[product_type][item_id] += quantity
            else:
                cart[product_type][item_id] = quantity
        else:
            cart[product_type] = {}
            cart[product_type][item_id] = quantity
    else:
        cart[product_type] = {}
        cart[product_type][item_id] = quantity

    # Overwrite session variable with updated one
    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the quantity of the specified product
    to the specified amount """

    if request.method == 'POST':

        redirect_url = request.POST.get('redirect_url')
        quantity = int(request.POST.get('quantity'))
        product_type = request.POST.get('product_type')

        cart = request.session.get('cart', {})
        cart[product_type][item_id] = quantity

        request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ Remove item from shopping cart """

    product_type = request.POST.get('product_type')

    if product_type == 'game':
        product = get_object_or_404(Edition, sku=item_id)
        title = product.friendly_name_full
    elif product_type == 'adoption':
        product = get_object_or_404(Package, sku=item_id)
        title = product.adoption.animal.title() + ' ' + product.friendly_name

    try:
        cart = request.session.get('cart', {})
        cart[product_type].pop(item_id)

        cart_item_len = sum(map(len, cart.values()))

        if cart_item_len == 0:
            # Delete shopping cart from session if no items are present
            # in order to prevent users from trying to go to checkout
            del request.session['cart']
        else:
            request.session['cart'] = cart

        if product_type == 'game':
            messages.success(
                request,
                f'Removed {title} from your cart'
            )
        elif product_type == 'adoption':
            messages.success(
                request,
                f'Removed {title} from your cart'
            )

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')

        return HttpResponse(status=500)
