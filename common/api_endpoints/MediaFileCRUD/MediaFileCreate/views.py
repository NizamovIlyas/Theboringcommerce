from rest_framework import generics, permissions
from .serializers import MediaFileCreateSerializer
from common.models import MediaFile

class MediaFileCreateView(generics.CreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileCreateSerializer
    permission_classes = [permissions.IsAuthenticated]  # adjust as needed
