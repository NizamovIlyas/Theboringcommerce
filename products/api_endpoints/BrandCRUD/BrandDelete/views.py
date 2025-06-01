from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin 
# GenericAPIView + DestroyModelMixin = DestroyAPIView

from rest_framework import permissions

from products.models import Brand
from .serializers import BrandDeleteSerializer


class BrandDeleteAPIView(GenericAPIView, DestroyModelMixin):
    queryset = Brand.objects.all()
    serializer_class = BrandDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)