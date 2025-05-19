from rest_framework.generics import ListAPIView
from products.models import Size
from .serializers import SizeListSerializer

class SizeListView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
