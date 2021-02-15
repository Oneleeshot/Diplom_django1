from django.contrib import admin
from .models import Category, Product, Cart, CartProduct

admin.site.register(Cart)
admin.site.register(CartProduct)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
