from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public': 'pk_test_51Q557pL217fSTufiTovb74Lv8nMbY2LCYqv8H0nehElZoFUgOwIF7Lxl752fO6se4k6kZJqR2i2rOIgzyEM8zDP100W0tXZFYU',
        'client_secret': 'test client secret',
    }


    return render(request, template, context)