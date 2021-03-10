from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('users', views.UserViewSet, basename='users')

