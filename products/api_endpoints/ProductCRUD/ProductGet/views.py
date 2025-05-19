from rest_framework import generics
from products.models import Product
from .serializers import ProductGetSerializer

class ProductGetView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductGetSerializer
    lookup_field = 'slug'
