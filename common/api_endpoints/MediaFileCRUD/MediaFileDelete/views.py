from rest_framework import generics, permissions
from common.models import MediaFile

class MediaFileDeleteView(generics.DestroyAPIView):
    queryset = MediaFile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
