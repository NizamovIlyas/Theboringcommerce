from rest_framework import serializers
from products.models import ProductVariant
from common.models import MediaFile

class MediaFileSerializerByProduct(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id',]

class ProductVariantListSerializerByProduct(serializers.ModelSerializer):
    images = MediaFileSerializerByProduct(many=True)

    class Meta:
        model = ProductVariant
        fields = [
            'id', 'name', 'price', 'stock', 'images',
            'color', 'size', 'is_active', 'created_at', 'updated_at'
        ]
