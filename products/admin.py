from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from .models import (
    Category, ProductType,
    Attribute, AttributeValue, Product, ProductVariant
)

admin.site.register([
    ProductType,
    Attribute, AttributeValue
])

admin.site.register(Category, MPTTModelAdmin)


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    fields = ['sku', 'name', 'price', 'quantity', 'quantity_allocated', 'images']


class ProductAdmin(admin.ModelAdmin):
    # 指定 InlineAdmin
    inlines = [
        ProductVariantInline,
    ]


admin.site.register(Product, ProductAdmin)