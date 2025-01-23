from django.db import models
from django.utils.text import slugify
from .supplier import Supplier
from .category import Category
from .mixins import CreateUpdateMixIn


class ColorVariant(CreateUpdateMixIn):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="color_images", null=True, blank=True)



    def __str__(self) -> str:
        return f"{self.color_name}"


class SizeVariant(CreateUpdateMixIn):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.size_name}"


class Product(CreateUpdateMixIn):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Products")
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    reorder_level = models.IntegerField(default=0)
    suppliers = models.ManyToManyField(Supplier, related_name="products")
    color_variant = models.ManyToManyField(ColorVariant, blank=True)
    size_variant = models.ManyToManyField(SizeVariant, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.product_name}"


    def get_product_price_by_size(self, size):
        return self.price + SizeVariant.objects.get(size_name=size).price

    def get_product_price_by_color(self, color):
        return self.price + ColorVariant.objects.get(color_name=color).price