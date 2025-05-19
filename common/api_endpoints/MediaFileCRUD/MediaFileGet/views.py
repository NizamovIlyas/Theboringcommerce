from rest_framework import generics, permissions
from .serializers import MediaFileGetSerializer
from common.models import MediaFile

class MediaFileDetailView(generics.RetrieveAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileGetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
