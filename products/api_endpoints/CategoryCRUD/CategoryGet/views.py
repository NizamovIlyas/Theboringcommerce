from rest_framework.generics import ListAPIView
from products.models import Category
from .serializers import CategoryListSerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
