from rest_framework import serializers
from products.models import Brand


class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name',
                'slug',
                'logo']
        
    def validate_logo(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Logo size should be less than 2MB")
        
        if not value.content_type.startwith('image/'):
            raise serializers.ValidationError("Content type is not image")
        return value