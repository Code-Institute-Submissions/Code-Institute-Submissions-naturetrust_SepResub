from checkout.models import Order
from django.shortcuts import render

from .forms import OrderForm


def checkout(request):
    """ A view to render the checkout page """

    form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
