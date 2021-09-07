from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from games.models import Edition


def cart_contents(request):
    """ A context processor for storing the
    contents of the shopping cart """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        game_edition = get_object_or_404(Edition, pk=item_id)
        total += quantity * game_edition.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'edition': game_edition,
        })

    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'total': total,
    }

    return context
