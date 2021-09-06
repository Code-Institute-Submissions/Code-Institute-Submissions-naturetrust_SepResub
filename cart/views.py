from django.shortcuts import get_object_or_404, render
from django.contrib import messages


def view_cart(request):
    """ A view that renders the shopping cart contents """

    return render(request, 'cart/cart.html')
