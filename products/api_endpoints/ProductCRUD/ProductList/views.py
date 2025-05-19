from rest_framework import generics
from products.models import Product
from .serializers import ProductListSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer
