from django.forms import ModelForm, ValidationError
from ..models import *


class ProductImageForm(ModelForm):

    class Meta:
        model = ProductImage
        fields = ['product', 'category_image']