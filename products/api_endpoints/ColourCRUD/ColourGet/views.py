from rest_framework.generics import ListAPIView
from products.models import Color
from .serializers import ColourListSerializer

class ColourListView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColourListSerializer
