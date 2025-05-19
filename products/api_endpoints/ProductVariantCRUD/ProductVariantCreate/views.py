from rest_framework import generics
from products.models import ProductVariant
from .serializers import ProductVariantCreateSerializer

class ProductVariantCreateView(generics.CreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantCreateSerializer
