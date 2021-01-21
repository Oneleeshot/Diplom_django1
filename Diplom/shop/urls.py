from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls import static

app_name = 'shop'

urlpatterns = [
                  path('', glasses,
                       name='home_page'),
                  path('glasses/', glasses,
                       name='glasses'),
                  path('sun/', sun_glasses,
                       name='sun_glasses'),
                  path('optical/', optical_glasses,
                       name='optical_glasses'),
                  path('sun/mens/', sun_mens_glasses,
                       name='sun_mens_glasses'),
                  path('sun/womens/', sun_womens_glasses,
                       name='sun_womens_glasses'),
                  path('optical/mens/', optical_mens_glasses,
                       name='optical_mens_glasses'),
                  path('optical/womens/', optical_womens_glasses,
                       name='optical_womens_glasses'),
                  path('<slug>/', ProductDetailView.as_view(),
                       name='product_detail'),
              ] + static.static(settings.STATIC_URL,
                                document_root=settings.STATIC_URL)
