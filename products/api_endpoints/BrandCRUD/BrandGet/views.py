from rest_framework.generics import CreateAPIView, ListAPIView
from products.models import Brand
from .serializers import BrandCreateSerializer, BrandListSerializer


class BrandCreateView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
