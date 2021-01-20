from django.urls import path

from . import views

app_name = 'products'


urlpatterns = [
    path('categories/<category_id>/', views.get_category, name='get_category'),
    path('<product_id>/', views.get_product, name='get_product'),
]