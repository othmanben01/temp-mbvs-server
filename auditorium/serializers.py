from .models import Auditorium, Video
from rest_framework import serializers


class AuditoriumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auditorium
        fields = "__all__"

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"