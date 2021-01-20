from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('oauth_login/', views.oauth_login),
    path('oauth_callback/', views.oauth_callback),
]