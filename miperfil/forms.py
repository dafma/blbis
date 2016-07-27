__author__ = 'mrk2'
from productos.models import Product, ProductImage
from django import forms

class CrearProdForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'categories')
        widgets = {
            "title": forms.TextInput(attrs={'class': 'input-text'}),
            "description": forms.Textarea(attrs={'class': 'input-text'}),
            "price": forms.TextInput(attrs={'class': 'input-text'}),

        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('product', 'image')


