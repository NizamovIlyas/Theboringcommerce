from rest_framework import serializers
from products.models import Product, Brand, Category
from common.models import MediaFile

class MediaFileSerializerForList(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id',]

class BrandSerializerForList(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo']

class CategorySerializerForList(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductListSerializer(serializers.ModelSerializer):
    brand = BrandSerializerForList()
    category = CategorySerializerForList()
    default_images = MediaFileSerializerForList(many=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description',
            'brand', 'category', 'default_images',
            'is_active', 'created_at', 'updated_at'
        ]
