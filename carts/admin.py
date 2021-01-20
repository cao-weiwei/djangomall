from django.contrib import admin

from .models import Cart, CartLine


class CartLineAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register(CartLine, CartLineAdmin)
admin.site.register(Cart)