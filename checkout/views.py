from django.shortcuts import render


def checkout(request):
    """ A view to render the checkout page """

    return render(request, 'checkout/checkout.html')
