from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from api.pagination import CustomPageNumberPagination
from api.permissions import IsUserOrReadOnly
from api.serializers import ProductSerializer, UserSerializer
from shop.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsUserOrReadOnly, )
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name", "type")


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )
