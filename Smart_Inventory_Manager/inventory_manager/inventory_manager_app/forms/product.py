from django.forms import ModelForm, ValidationError
from ..models import Product, ProductImage
from django.forms import inlineformset_factory
from django import forms  # Import forms module
from django.utils.translation import gettext as _


class ProductModelCreateForm(ModelForm):

    def clean_name(self):
        name = self.cleaned_data.get('product_name')
        if not name:
            raise ValidationError(_('Please provide a valid name for new product.'))
        if len(name) < 3:
            raise ValidationError(_('Looks like this product name is too short...'))
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError(_('Price must be a positive number.'))

        return price

    class Meta:
        model = Product
        fields = [
            'product_name',
            'category',
            'description',
            'price',
            'stock_quantity',
            'reorder_level',
            'suppliers',
        ]
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'reorder_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'suppliers': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }



class ProductModelUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'category',
            'description',
            'price',
            'stock_quantity',
            'reorder_level',
            'suppliers',
        ]