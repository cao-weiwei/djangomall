from django.contrib import admin
from django.urls import path

from .views import *

from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('books/', show_book_info),
    # path('api/', show_book_info),
]

# 路由Router：动态生成视图集中API处理函数的url地址的配置项
router = DefaultRouter()  # 可以处理视图的路由器
router.register('books', BookInfoViewSet, basename='books')  # 向路由器中注册视图集
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中