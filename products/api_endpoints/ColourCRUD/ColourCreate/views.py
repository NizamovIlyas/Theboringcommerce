from rest_framework.generics import CreateAPIView
from products.models import Color
from .serializers import ColourCreateSerializer

class ColourCreateView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColourCreateSerializer
