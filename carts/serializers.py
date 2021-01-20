from rest_framework import serializers

from .models import CartLine
# 导入商品变种序列化器
from products.serializers import ProductVariantSerializer


class CartLineSerializer(serializers.ModelSerializer):
    # 增加字段返回商品变种详细信息
    product_variant_details = ProductVariantSerializer(
        source='product_variant',
        read_only=True
    )
    # 增加 total 字段，返回购物车条目模型的 get_total() 的值
    total = serializers.DecimalField(
        max_digits=16,
        decimal_places=2,
        source='get_total',
        read_only=True
    )

    class Meta:
        model = CartLine
        # 序列化全部字段
        fields = '__all__'

