from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:order_id>/', views.update_order, name='update'),
]
