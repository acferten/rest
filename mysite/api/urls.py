from django.urls import path
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('user/<int:pk>', DetailUser.as_view(), name='profile'),
    path('login', views.obtain_auth_token),
    path('signup', SignUp.as_view(), name="signup"),

    path('products', ProductList.as_view(), name='products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product'),
    path('products/<int:pk>/order', CreateOrder.as_view(), name='order'),
]
