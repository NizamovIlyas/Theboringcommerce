from rest_framework import serializers
from common.models import MediaFile

class MediaFileGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'file', 'file_type', 'alt_text', 'created_at', 'updated_at']
