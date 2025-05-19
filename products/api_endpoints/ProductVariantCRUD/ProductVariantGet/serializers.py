from rest_framework import serializers
from products.models import ProductVariant
from common.models import MediaFile
from products.models import Color, Size

class MediaFileSerializerForVariantGet(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id',]

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'slug']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name', 'slug']

class ProductVariantGetSerializer(serializers.ModelSerializer):
    images = MediaFileSerializerForVariantGet(many=True)
    color = ColorSerializer()
    size = SizeSerializer()

    class Meta:
        model = ProductVariant
        fields = [
            'id', 'name', 'price', 'stock', 'images',
            'color', 'size', 'is_active', 'created_at', 'updated_at'
        ]
