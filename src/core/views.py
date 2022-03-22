from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Athlet
from core.serializers import AthletSerializer

class AthletsListCreateAPI(ListCreateAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer

class AthletsUpdateAPI(UpdateAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer

class AthletsRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer