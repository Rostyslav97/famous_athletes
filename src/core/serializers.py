from rest_framework import serializers
from core.models import Athlet

class AthletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlet
        fields = "__all__"