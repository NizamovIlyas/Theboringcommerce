from rest_framework import serializers
from products.models import Product, Brand, Category
from common.models import MediaFile

class MediaFileSerializerForGet(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id',]  # adjust to your MediaFile model

class BrandSerializerForProductGet(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug']

class CategorySerializerForGet(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductGetSerializer(serializers.ModelSerializer):
    brand = BrandSerializerForProductGet(read_only=True)
    category = CategorySerializerForGet(read_only=True)
    default_images = MediaFileSerializerForGet(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'slug', 'brand', 'default_images', 
            'category', 'is_active', 'created_at', 'updated_at'
        ]
