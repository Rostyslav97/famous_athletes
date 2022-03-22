from urllib import request
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
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Athlet.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        
        serializer = AthletSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data}) 