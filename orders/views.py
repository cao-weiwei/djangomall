from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from accounts.models import Address
from .models import Order, OrderStatus

from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

import django_filters


class OrderFilter(django_filters.FilterSet):
    paginate_by = 2

    class Meta:
        model = Order
        fields = ['created_at', 'id', 'status']


@login_required
def index(request):
    if request.method == 'POST':
        # 获取用户的购物车
        cart = request.user.carts.first()
        # 获取用户选择的收货地址
        shipping_address = get_object_or_404(
            Address,
            pk=request.POST.get('shipping_address')
        )
        # 创建订单
        order = Order.objects.create(
            shipping_address=shipping_address,
            user=cart.user
        )
        # 遍历购物车条目
        for line in cart.lines.all():
            # 通过购物车条目创建订单条目
            order.lines.create(
                product_variant=line.product_variant,
                product_sku=line.product_variant.sku,
                quantity=line.quantity,
                unit_price=line.unit_price,
                product_name=line.product_variant.product.name
            )
            order.total += line.get_total()
        order.save()
    order_filter = OrderFilter(request.GET, queryset=request.user.orders.all())

    paginator = Paginator(order_filter.qs, 2)
    page = request.GET.get('page')
    orders = paginator.get_page(page)
    ctx = {
        'order_filter': order_filter,
        'orders': orders,
    }
    return TemplateResponse(request, 'orders/index.html', ctx)


@login_required
def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.status = OrderStatus.CANCELED
    order.save()
    return redirect('orders:index')
