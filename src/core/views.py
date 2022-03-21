from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Athlet
from core.serializers import AthletSerializer

class AthletsAPIView(APIView):
    def get(self, request):
        a = Athlet.objects.all()
        return Response({'posts': AthletSerializer(a, many=True).data})

    def post(self, request):
        serializer = AthletSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Athlet.objects.create(name=request.data['name'], about=request.data['about'], category_id=request.data['category_id'])
        return Response({'post': AthletSerializer(post_new).data})
