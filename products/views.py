from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from .models import Product, Category, Attribute

from django.core.paginator import Paginator

from rest_framework import generics
from .serializers import ProductSerializer


def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # 查找商品所属的商品类型的所有属性
    attributes = Attribute.objects.filter(product_type=product.product_type)
    ctx = {
        'product': product,
        'attributes': attributes,
    }
    return TemplateResponse(request, 'products/get_product.html', ctx)


def get_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = category.get_descendants(include_self=True)
    products = Product.objects.filter(category__in=categories)
    # 对 products 进行分页，每页 1 条数据
    paginator = Paginator(products, 1)
    # 从 GET 请求获取页码
    page = request.GET.get('page')
    # 当前页的数据
    products = paginator.get_page(page)
    ctx = {
        'category': category,
        'products': products,
    }
    return TemplateResponse(request, 'products/get_category.html', ctx)


class ProductAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
