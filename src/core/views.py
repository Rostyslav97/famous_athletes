from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.models import Athlet
from core.serializers import AthletSerializer
from core.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class AthletsListCreateAPI(ListCreateAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AthletsRetrieveUpdateAPI(RetrieveUpdateAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer
    permission_classes = (IsOwnerOrReadOnly, ) 


class AthletsRetrieveDestroyAPI(RetrieveDestroyAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer
    permission_classes = (IsAdminOrReadOnly, ) 