from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from products.models import Brand
from .serializers import BrandListSerializer


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = [permissions.IsAuthenticated]


class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "slug"