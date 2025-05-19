from rest_framework import serializers
from products.models import Color

class ColourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'slug']
