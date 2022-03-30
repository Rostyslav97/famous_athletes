from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from core.models import Athlet
from core.serializers import AthletSerializer
from core.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination


class AthletsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class AthletsListCreateAPI(ListCreateAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = AthletsAPIListPagination


class AthletsRetrieveUpdateAPI(RetrieveUpdateAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )


class AthletsRetrieveDestroyAPI(RetrieveDestroyAPIView):
    queryset = Athlet.objects.all()
    serializer_class = AthletSerializer
    permission_classes = (IsAdminOrReadOnly, ) 
    