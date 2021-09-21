from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'date',
        'order_total', 'grand_total',
    )

    fields = (
        'order_number', 'date',
        'first_name', 'last_name',
        'email', 'phone_number', 'street_address',
        'street_address_2', 'town_or_city', 'country',
        'county', 'postcode',
        'order_total', 'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
