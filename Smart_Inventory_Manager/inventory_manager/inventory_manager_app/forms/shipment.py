from django.forms import ModelForm, ValidationError
from django.utils.translation import gettext as _
from ..models import *

class ShipmentModelCreateForm(ModelForm):

    def clean_name(self):
        name = self.cleaned_data.get('recipient_name')
        if not name:
            raise ValidationError(_('Please provide a valid name for new product.'))
        if len(name) < 3:
            raise ValidationError(_('Looks like this product name is too short...'))
        return name

    class Meta:
        model = Shipment
        fields = [
            'recipient_name',
            'order',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'postal_code',
            'country',
            'phone',
        ]