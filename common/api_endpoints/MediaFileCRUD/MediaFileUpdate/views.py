from rest_framework import generics, permissions
from .serializers import MediaFileUpdateSerializer
from common.models import MediaFile

class MediaFileUpdateView(generics.UpdateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
