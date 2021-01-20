from django.db import models
from django.conf import settings

from products.models import ProductVariant

from django.core.validators import MinValueValidator

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    """ 购物车模型
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='carts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.get_username()


class CartLine(models.Model):
    """ 购物车条目模型
    """
    cart = models.ForeignKey(
        Cart,
        related_name='lines',
        on_delete=models.CASCADE
    )
    # 购买的商品变种
    product_variant = models.ForeignKey(
        ProductVariant,
        related_name='+',
        on_delete=models.CASCADE
    )
    # 购买的商品变种数量，增加验证器，最小值 1
    quantity = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1)]
    )
    # 商品单价
    unit_price = models.DecimalField(max_digits=16, decimal_places=2)
    # 购物车条目的创建时间
    created_at = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        # 验证购物车+商品变种的组合唯一性
        unique_together = ('cart', 'product_variant')
        # 按照创建时间倒序排列
        ordering = ['-created_at']

    def __str__(self):
        return '{0} {1}({2})'.format(
            self.product_variant.product.name,
            self.product_variant.sku,
            self.quantity
        )

    def get_total(self):
        return self.unit_price * self.quantity

    def clean(self):
        # 检查如果购物车条目的数量大于商品变种库存，抛出异常
        if self.quantity > self.product_variant.quantity:
            raise ValidationError(
                _('Ensure this value is less than or equal to %(limit_value)s'),
                params={'limit_value': self.product_variant.quantity}
            )

    def save(self, *args, **kwargs):
        # 执行检查，包括 .clean()
        self.full_clean()
        return super().save(*args, **kwargs)
