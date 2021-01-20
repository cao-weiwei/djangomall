from rest_framework import serializers

from .models import Product, ProductVariant


class ProductVariantSerializer(serializers.ModelSerializer):
    """ 使用 ModelSerializer 序列化商品变种模型
    """
    class Meta:
        model = ProductVariant
        fields = ('id', 'name', 'sku', 'base_price', 'product_name', 'images')


class ProductSerializer(serializers.ModelSerializer):
    """ 同样使用 ModelSerializer 序列化商品模型，将商品变种模型作为字段返回
    """
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'price', 'variants')
