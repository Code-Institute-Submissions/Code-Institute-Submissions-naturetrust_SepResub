from django.shortcuts import get_object_or_404, render, redirect

from games.models import Edition


def view_cart(request):
    """ A view that renders the shopping cart contents """

    return render(request, 'cart/cart.html')


def add_to_cart(request, game_id):
    """ Add game and its quanitity
    to shopping cart """

    game_edition = get_object_or_404(Edition, pk=game_id)

    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    # Add game to shopping cart or update quantity if it already exists
    if game_id in list(cart.keys()):
        cart[game_id] += quantity
    else:
        cart[game_id] = quantity

    # Overwrite session variable with updated one
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
