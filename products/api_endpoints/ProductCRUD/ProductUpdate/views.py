from rest_framework import generics
from products.models import Product
from .serializers import ProductUpdateSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    lookup_field = 'slug'
