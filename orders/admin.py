from django.contrib import admin

from .models import Order, OrderLine


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    fields = ('product_name', 'product_sku', 'quantity', 'unit_price')


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderLineInline
    ]
    # 指定列表显示的字段
    list_display = ('id', 'user', 'created_at', 'total', 'status')
    # 搜索的字段
    search_fields = ('user__email', 'shipping_address__phone')
    # 过滤的字段
    list_filter = (
        'created_at',
        'user__email',
        'status'
    )


admin.site.register(Order, OrderAdmin)
