from rest_framework import generics
from products.models import Product
from .serializers import ProductCreateSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
