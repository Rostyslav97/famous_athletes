from rest_framework.generics import ListAPIView
from core.models import Athlet
from core.serializers import AthletSerializer

class AtheltsAPIView(ListAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer