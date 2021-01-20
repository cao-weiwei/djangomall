from django.db import models

from mptt.managers import TreeManager
from mptt.models import MPTTModel


class Category(MPTTModel, models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE)

    tree = TreeManager()

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """ 商品类型
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    """ 商品类型的属性，和商品类型一对多
    """
    name = models.CharField(max_length=128)
    product_type = models.ForeignKey(
        ProductType,
        related_name='product_attributes',
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    """ 商品类型属性的值，和商品类型属性一对多
    """
    attribute = models.ForeignKey(
        Attribute,
        related_name='values',
        on_delete=models.CASCADE)
    value = models.CharField(max_length=32)

    def __str__(self):
        return self.value


class Product(models.Model):
    """ 商品模型。包含多个商品类型属性的值
    """
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE)
    product_type = models.ForeignKey(
        ProductType,
        related_name='products',
        on_delete=models.CASCADE)
    attribute_values = models.ManyToManyField('AttributeValue')
    name = models.CharField(max_length=128)
    # 商品价格
    price = models.DecimalField(max_digits=16, decimal_places=2)
    # 商品图片
    image = models.ImageField(upload_to='products')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='variants',
        on_delete=models.CASCADE)
    sku = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    images = models.ImageField(upload_to='products')
    # 库存数量
    quantity = models.PositiveIntegerField(default=0)
    quantity_allocated = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '-'.join([self.sku, self.name])

    @property
    def base_price(self):
        """ 商品变种的价格，如果为空，取商品的价格
        """
        return self.price or self.product.price

    @property
    def product_name(self):
        return self.product.name
