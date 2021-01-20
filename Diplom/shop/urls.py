from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls import static


app_name = 'shop'

urlpatterns = [
    path('', home, name='home_page'),
    path('sun/', sun_glasses, name='sun_glasses'),
    path('<slug>/', ProductDetailView.as_view(), name='product_detail'),
] + static.static(settings.STATIC_URL, document_root=settings.STATIC_URL)

