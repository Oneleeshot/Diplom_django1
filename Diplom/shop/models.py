from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("shop:category-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True,
                              null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    available = models.BooleanField(default=True, null=True)
    type = models.CharField(max_length=50, default=" ")

    class Meta:
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return reverse("shop:product-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 325 or img.width > 155:
            output_size = (325, 155)
            img.thumbnail(output_size)
            img.save(self.image.path)


class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE,
                             related_name='related_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True,
                                      related_name='related_cart')
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)
