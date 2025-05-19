from rest_framework import generics
from products.models import Product

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'slug'
