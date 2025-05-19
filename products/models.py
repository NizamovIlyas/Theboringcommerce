from django.db import models
from common.models import BaseModel  

class Brand(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True, null=False, blank=False)
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Size(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Color(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    slug = models.SlugField(unique=True, null=False, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    default_images = models.ManyToManyField('common.MediaFile', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants', null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)
    stock = models.IntegerField(default=0, null=False, blank=False)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_variants')
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_variants')
    images = models.ManyToManyField('common.MediaFile', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} - {self.name} - {self.price}"
