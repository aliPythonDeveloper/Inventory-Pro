from django.db import models
from django.utils.text import slugify
from .product import Product
from .mixins import CreateUpdateMixIn



class ProductImage(CreateUpdateMixIn):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products_image")
    category_image = models.ImageField(upload_to="products")