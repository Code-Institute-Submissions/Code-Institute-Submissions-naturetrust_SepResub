import uuid

from django.db import models
from django.db.models import Sum

from django_countries.fields import CountryField

from games.models import Edition
from adoption.models import Adoption, Package


class Product(models.Model):
    game = models.ForeignKey(
        Edition,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    adoption = models.ForeignKey(
        Package,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='', null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID  """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total each time a line item is added """

        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total_sum']

        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """ Override original save method to set order number """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)

    quantity = models.IntegerField(null=True, blank=True, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """ Override original save method to set order number """

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
