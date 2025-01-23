from django.db import models
from django.contrib.auth.models import User
from .mixins import CreateUpdateMixIn

class wholeSaler(CreateUpdateMixIn):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wholesaler')
    company_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.company_name