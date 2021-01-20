from django.urls import path, include
from rest_framework import routers

from products.views import ProductAPIView
# 导入 CartLineViewSet
from carts.views import CartLineViewSet

app_name = 'api'


# 设置路由
router = routers.SimpleRouter()
router.register(r'cartlines', CartLineViewSet, 'cartlines')

urlpatterns = [
    # 加入 urlpatterns
    path('', include(router.urls)),
    path('products/<id>/', ProductAPIView.as_view())
]
