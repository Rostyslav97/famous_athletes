from email.policy import default
from rest_framework import serializers
from core.models import Athlet


class AthletSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Athlet
        fields = "__all__"
