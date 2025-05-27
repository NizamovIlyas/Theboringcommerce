from rest_framework import serializers
from products.models import Product, Brand, Category
from common.models import MediaFile
from products.utils import slugify

class CategoryProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug"
        ]


class ProductCreateSerializer(serializers.ModelSerializer):
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
            "category": CategoryProductCreateSerializer(instance.category).data
                   }

        return instance

    def create(self, validated_data):
        is_exists = Product.objects.filter(slug=slugify(validated_data["name"])).exists()
        if is_exists:
            return serializers.ValidationError("Product with this name already exists (or deactivated).")

        return Product.objects.create(
            slug = slugify(validated_data["name"]),
            **validated_data
        )