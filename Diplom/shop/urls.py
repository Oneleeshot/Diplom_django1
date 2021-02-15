from django.urls import path

from . import views
from .views import *
from django.conf import settings
from django.conf.urls import static

app_name = 'shop'

urlpatterns = [
                  path('',
                       views.GlassesView.as_view(),
                       name='home_page'),
                  path('glasses/',
                       views.GlassesView.as_view(),
                       name='glasses'),
                  path('sun/',
                       views.SunGlassesView.as_view(),
                       name='sun_glasses'),
                  path('optical/',
                       views.OpticalGlassesView.as_view(),
                       name='optical_glasses'),
                  path('sun/mens/',
                       views.SunMenGlassesView.as_view(),
                       name='sun_mens_glasses'),
                  path('sun/womens/',
                       views.SunWomenGlassesView.as_view(),
                       name='sun_womens_glasses'),
                  path('optical/mens/',
                       views.OpticalManGlassesView.as_view(),
                       name='optical_mens_glasses'),
                  path('optical/womens/',
                       views.OpticalWomenGlassesView.as_view(),
                       name='optical_womens_glasses'),
                  path('<slug>/',
                       views.product_detail,
                       name='product_detail'),

              ] + static.static(settings.STATIC_URL,
                                document_root=settings.STATIC_URL)
