from rest_framework.generics import RetrieveAPIView
from .models import OpenDay
from .serializers import OpenDaySerializer

class OpenDayDetailView(RetrieveAPIView):
    lookup_field = "slug"
    queryset = OpenDay.objects.all()
    serializer_class = OpenDaySerializer