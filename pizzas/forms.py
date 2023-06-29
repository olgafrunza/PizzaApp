from django import forms
from .models import Order


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'quantity',
        )
