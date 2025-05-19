from rest_framework import generics
from products.models import ProductVariant
from .serializers import ProductVariantListSerializerForList

class ProductVariantListView(generics.ListAPIView):
    serializer_class = ProductVariantListSerializerForList

    def get_queryset(self):
        queryset = ProductVariant.objects.all()
        product_id = self.request.query_params.get('product')
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset
