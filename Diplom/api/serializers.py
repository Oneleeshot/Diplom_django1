from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'link', 'description', 'image',
                  'price', 'type', 'available']

    def get_link(self, obj):
        uri = reverse("products-detail", kwargs={"pk": obj.pk})
        return self.context["request"].build_absolute_uri(uri)


class UserSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username', 'id', 'link', 'email', 'first_name', 'last_name']

    def get_link(self, obj):
        uri = reverse("users-detail", kwargs={"pk": obj.pk})
        return self.context["request"].build_absolute_uri(uri)