# menu/forms.py
from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['nama', 'harga', 'deskripsi', 'gambar']
