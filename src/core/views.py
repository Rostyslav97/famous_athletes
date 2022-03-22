from rest_framework.viewsets import ModelViewSet
from core.models import Athlet
from core.serializers import AthletSerializer


class AthletViewSet(ModelViewSet):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer 
