from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from core.models import Athlet, Category
from core.serializers import AthletSerializer
from rest_framework.response import Response

class AthletViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Athlet.objects.all()
    serializer_class = AthletSerializer 

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Athlet.objects.all()[:3]
        return Athlet.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
