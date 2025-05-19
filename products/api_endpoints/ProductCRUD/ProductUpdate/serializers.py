from rest_framework import serializers
from products.models import Product, Brand, Category
from common.models import MediaFile

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
