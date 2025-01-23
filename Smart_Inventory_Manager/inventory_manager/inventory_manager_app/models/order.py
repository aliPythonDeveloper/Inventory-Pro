from datetime import timezone
from django.utils import timezone

from django.db import models
from django.utils.text import slugify
from .mixins import CreateUpdateMixIn

from .product import Product
from .wholesaler import wholeSaler
from .cart import Cart
class Order(CreateUpdateMixIn):
    ORDER_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    order_id = models.AutoField(primary_key=True)
    wholesaler = models.ForeignKey(wholeSaler, on_delete=models.CASCADE, related_name="wholesaler")
    cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default="Pending")

    def __str__(self) -> str:
        return f"Order {self.order_id}"

    @property
    def calculate_total(self):
        total = sum(item.total_price() for item in self.cart.items.all())
        return total
    @property
    def get_cart_items(self):
        return self.cart.items.all()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.product.product_name} - {self.quantity} pcs"

    @property
    def total_price(self):
        return self.product.price * self.quantity