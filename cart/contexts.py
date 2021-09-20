from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings

from games.models import Edition
from adoption.models import Adoption, Package


def cart_contents(request):
    """ A context processor for storing the
    contents of the shopping cart """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for product_type in cart.items():
        if 'game' in product_type:
            for item in product_type:
                if isinstance(item, dict):
                    for item_id, quantity in item.items():
                        product = get_object_or_404(Edition, sku=item_id)
                        subtotal = quantity * product.price
                        total += quantity * product.price
                        product_count += quantity
                        cart_items.append({
                            'item_id': item_id,
                            'product': product,
                            'product_type': product_type,
                            'quantity': quantity,
                            'subtotal': subtotal,
                        })
        elif 'adoption' in product_type:
            for item in product_type:
                if isinstance(item, dict):
                    for item_id, quantity in item.items():
                        product = get_object_or_404(Package, sku=item_id)
                        subtotal = quantity * product.price
                        total += quantity * product.price
                        product_count += quantity
                        cart_items.append({
                            'item_id': item_id,
                            'product': product,
                            'product_type': product_type,
                            'quantity': quantity,
                            'subtotal': subtotal,
                        })

    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'total': total,
    }

    return context
