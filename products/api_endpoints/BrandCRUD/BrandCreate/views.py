from rest_framework.generics import CreateAPIView
from products.models import Brand
from .serializers import BrandCreateSerializer


class BrandCreateView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer 