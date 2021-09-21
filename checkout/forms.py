from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = (
            'order_number', 'date',
            'order_total', 'grand_total',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.fields[field].required:
                label = f'{field} *'
                self.fields[field].label = label
            else:
                label = f'{field}'
                self.fields[field].label = label
