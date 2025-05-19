from rest_framework import serializers
from .models import MediaFile

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'file']  # Only the fields in your model
