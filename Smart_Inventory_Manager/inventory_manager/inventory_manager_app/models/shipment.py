from .mixins import CreateUpdateMixIn
from django.db import models
from .order import *

class Shipment(CreateUpdateMixIn):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name = "shipment", blank=True, null=True)
    recipient_name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)  # Optional
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Optional

    def __str__(self) -> str:
        return f"Shipment for Order #{self.recipient_name}"