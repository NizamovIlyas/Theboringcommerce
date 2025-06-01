from rest_framework.generics import CreateAPIView
from rest_framework import permissions, parsers
from products.models import Brand
from .serializers import BrandCreateSerializer


class BrandCreateView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer 
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]