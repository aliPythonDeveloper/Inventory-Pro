from rest_framework import serializers
from ..models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields  = ["category_image"]

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["user"]

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = ["color_name", "price", "image"]

class SizeVariant(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = ["size_name", "price"]


class ProductSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)
    products_image = ProductImageSerializer(many=True, read_only=True)  # Include all images related to the product
    color_variant = ColorSerializer(many=True, read_only=True)  # Include all images related to the product
    size_variant = SizeVariant(many=True, read_only=True)  # Include all images related to the product

    class Meta:
        model = Product
        fields = [
            'product_name',
            'category',
            'description',
            'price',
            'stock_quantity',
            'reorder_level',
            'suppliers',
            "products_image",
            "color_variant",
            "size_variant"
        ]