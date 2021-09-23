from profiles.models import UserProfile
from django import http
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from django.contrib.auth.models import User
from .models import Order, OrderLineItem, Product
from games.models import Edition
from adoption.models import Package

import json
import time


class StripeWH_Handler:
    """ Handle Stripe Hooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send user a confirmation email """

        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """ Handle a generic/unknown unexpected webhook event """

        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook from Stripe """

        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Replace empty strings with None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update user profile if save_info is checked

        # To allow anoynmous users to checkout
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address = shipping_details.address.line1
                profile.default_street_address_2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state

                profile.save()

        order_exists = False

        # Create a delay incase the view is slow
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_details.name.split(' ')[0],
                    last_name__iexact=shipping_details.name.split(' ')[1],
                    user_profile=profile,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                # If the order is found, break out of the loop
                break
            # If the order isn't found then increment attempt and
            # use Python's time module to sleep for one second
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            # Send confirmation email before returning a response to stripe
            self._send_confirmation_email(order)

            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Verified order already in database',
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name__iexact=shipping_details.name.split(' ')[0],
                    last_name__iexact=shipping_details.name.split(' ')[1],
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for product_type in cart.items():
                    if 'game' in product_type:
                        for item in product_type:
                            if isinstance(item, dict):
                                for item_id, qty in item.items():
                                    game = Edition.objects.get(sku=item_id)
                                    try:
                                        product = Product.objects.get(sku=item)
                                    except Product.DoesNotExist:
                                        product = Product.objects.create(
                                            sku=item_id,
                                            game=game,
                                            price=game.price
                                        )
                                    order_line_item = OrderLineItem(
                                        order=order,
                                        product=product,
                                        quantity=qty,
                                    )
                                    order_line_item.save()
                    elif 'adoption' in product_type:
                        for item in product_type:
                            if isinstance(item, dict):
                                for item_id, qty in item.items():
                                    adoption = Package.objects.get(sku=item_id)
                                    try:
                                        product = Product.objects.get(
                                            sku=item_id)
                                    except Product.DoesNotExist:
                                        product = Product.objects.create(
                                            sku=item_id,
                                            adoption=adoption,
                                            price=adoption.price
                                        )
                                    order_line_item = OrderLineItem(
                                        order=order,
                                        product=product,
                                        quantity=qty,
                                    )
                                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()

                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
                    status=500
                )
        # Send confirmation email before returning a response to stripe
        self._send_confirmation_email(order)

        return HttpResponse(
            content=f'Webhook recieved: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
