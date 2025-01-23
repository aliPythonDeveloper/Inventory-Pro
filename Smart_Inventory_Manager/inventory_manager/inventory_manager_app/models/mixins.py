from django.db import models
from django.utils import timezone

class CreateUpdateMixIn(models.Model):
    """
    Implements a created and an updated field to a base Django Model.

    Attributes
    ----------
    created: datetime
        A created timestamp. Defaults to now().
    updated: str
        An updated timestamp used to identify when models are updated.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def clean(self):
        super().clean()