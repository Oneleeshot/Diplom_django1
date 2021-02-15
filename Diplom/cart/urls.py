from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<slug>/', views.cart_add, name='cart_add'),
    path('remove/<slug>/', views.cart_remove,
         name='cart_remove'),
]
