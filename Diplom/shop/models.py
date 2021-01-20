from django.db import models
from django.shortcuts import reverse
from PIL import Image

# Create your models here.


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

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
