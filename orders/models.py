from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from accounts.models import Address
from products.models import ProductVariant
from .tasks import send_order_mail

import uuid


class OrderStatus:
    UNFULFILLED = 'unfulfilled'
    FULFILLED = 'fulfilled'
    CANCELED = 'canceled'

    CHOICES = [
        (UNFULFILLED, '未完成'),
        (FULFILLED, '已完成'),
        (CANCELED, '已取消'),
    ]


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name='orders',
        on_delete=models.SET_NULL)
    # 收货地址
    shipping_address = models.ForeignKey(
        Address, related_name='+', editable=False, null=True,
        on_delete=models.SET_NULL)
    # 订单备注
    customer_note = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    status = models.CharField(
        max_length=32, default=OrderStatus.UNFULFILLED,
        choices=OrderStatus.CHOICES)

    def save(self, *args, **kwargs):
        # 传递字典格式的参数
        send_order_mail.delay({'id': self.pk, 'total': self.total})
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order, related_name='lines', editable=False, on_delete=models.CASCADE)
    # 商品变种
    product_variant = models.ForeignKey(ProductVariant,
                                        related_name='order_lines',
                                        blank=True,
                                        null=True,
                                        on_delete=models.SET_NULL)
    # 商品名
    product_name = models.CharField(max_length=256)
    # 商品 sku
    product_sku = models.CharField(max_length=32)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=16, decimal_places=2)

    def get_total(self):
        return self.unit_price * self.quantity
