from django.urls import path
from ..views.shipment import *

urlpatterns = [
    path('add-shipment/', ShipmentModelCreateView.as_view(), name='add-shipment'),
]
