from django.urls import path

from . import views
from .views import *
from django.conf import settings
from django.conf.urls import static

app_name = 'shop'

urlpatterns = [
                  path('glasses/',
                       views.GlassesView.as_view(),
                       name='glasses'),
                  path('glasses/<str:type>/',
                       views.GlassesView.as_view(),
                       name='home_page'),
                  path('glasses/<str:type>/<int:category>/',
                       views.GlassesView.as_view(),
                       name='glasses'),
                  path('<slug>/',
                       views.product_detail,
                       name='product_detail'),

              ] + static.static(settings.STATIC_URL,
                                document_root=settings.STATIC_URL)
