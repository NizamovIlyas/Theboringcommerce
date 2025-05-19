from rest_framework import generics
from products.models import ProductVariant
from .serializers import ProductVariantGetSerializer

class ProductVariantDetailView(generics.RetrieveAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantGetSerializer
    lookup_field = 'id'
