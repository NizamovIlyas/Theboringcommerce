from rest_framework import serializers
from products.models import Product, Brand, Category
from common.models import MediaFile
from products.utils import *



class CategoryProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug"
        ]


class ProductUpdateSerializer(serializers.ModelSerializer):
    default_images = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MediaFile.objects.all(), required=False
    )
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), required=False, allow_null=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, allow_null=True)
    
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'slug', 'brand', 'default_images', 'category',
            'is_active'
        ]
    def to_representation(self, instance):
        instance = {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            "brand": instance.brand.name,
            "slug": instance.slug,
            "is_active": instance.is_active,
            "category": CategoryProductUpdateSerializer(instance.category).data
        }

        return instance

    def update(self, instance, validated_data):
        if "name" in validated_data:
            validated_data["slug"] = slugify(validated_data["name"])
        return super().update(instance, validated_data)