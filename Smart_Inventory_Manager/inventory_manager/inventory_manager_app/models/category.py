from django.db import models
from django.utils.text import slugify
from .mixins import CreateUpdateMixIn


class Category(CreateUpdateMixIn):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategories'
    )
    category_image = models.ImageField(upload_to="categories", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.category_name}"
