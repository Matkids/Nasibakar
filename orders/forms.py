# orders/forms.py

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # atau sebutkan field tertentu, misal: ['menu', 'quantity', 'customer_name']
