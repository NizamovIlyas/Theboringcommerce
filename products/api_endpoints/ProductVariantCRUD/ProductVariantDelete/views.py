from rest_framework import generics
from products.models import ProductVariant

class ProductVariantDeleteView(generics.DestroyAPIView):
    queryset = ProductVariant.objects.all()
    lookup_field = 'id'
