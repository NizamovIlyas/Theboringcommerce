from rest_framework import generics
from products.models import ProductVariant
from .serializers import ProductVariantUpdateSerializer

class ProductVariantUpdateView(generics.UpdateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantUpdateSerializer
    lookup_field = 'id'
