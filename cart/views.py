from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib import messages

from games.models import Edition


def view_cart(request):
    """ A view that renders the shopping cart contents """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add game and its quanitity
    to shopping cart """

    game_edition = get_object_or_404(Edition, pk=item_id)

    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    # Add game to shopping cart or update quantity if it already exists
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    # Overwrite session variable with updated one
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the quantity of the specified product
    to the specified amount """

    if request.method == 'POST':

        redirect_url = request.POST.get('redirect_url')
        quantity = int(request.POST.get('quantity'))

        cart = request.session.get('cart', {})
        cart[item_id] = quantity

        request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ Remove item from shopping cart """

    game_edition = get_object_or_404(Edition, pk=item_id)

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        messages.success(
            request,
            f'Removed {game_edition.friendly_name_full} from your cart'
        )

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')

        return HttpResponse(status=500)
