from rest_framework import serializers

class AthletSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    about = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()
