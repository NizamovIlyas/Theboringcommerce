from rest_framework.generics import CreateAPIView
from products.models import Category
from .serializers import CategoryCreateSerializer

class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
