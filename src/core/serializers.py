from rest_framework import serializers
from core.models import Athlet

class AthletSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    about = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Athlet.objects.create(**validated_data) 

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.about = validated_data.get("about", instance.about)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.save()
        return instance