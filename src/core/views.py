from django.forms import model_to_dict
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Athlet
from core.serializers import AthletSerializer

class AthletsAPIView(APIView):
    def get(self, request):
        lst = Athlet.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Athlet.objects.create(name=request.data['name'], about=request.data['about'], category_id=request.data['category_id'])
        return Response({'post': model_to_dict(post_new)})

# class AthletsAPIView(ListAPIView):
#     queryset = Athlet.objects.all()
#     serializer_class = AthletSerializer