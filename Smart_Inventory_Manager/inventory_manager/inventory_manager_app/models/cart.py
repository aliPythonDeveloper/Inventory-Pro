from django.contrib.auth.models import User
from django.db import models
from .mixins import CreateUpdateMixIn
from .product import Product

class Cart(CreateUpdateMixIn):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user}"

    @property
    def total_price(self):
        # Sum the total price of all cart items
        return sum(item.total_price for item in self.items.all())

class CartItem(CreateUpdateMixIn):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product.product_name} - {self.quantity} pcs"

    @property
    def total_price(self):
        return self.product.price * self.quantity