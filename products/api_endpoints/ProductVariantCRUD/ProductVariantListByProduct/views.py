from rest_framework import generics
from products.models import ProductVariant
from .serializers import ProductVariantListSerializerByProduct

class ProductVariantListByProductView(generics.ListAPIView):
    serializer_class = ProductVariantListSerializerByProduct

    def get_queryset(self):
        product_id = self.request.query_params.get('product')
        if product_id:
            return ProductVariant.objects.filter(product_id=product_id)
        return ProductVariant.objects.none()
