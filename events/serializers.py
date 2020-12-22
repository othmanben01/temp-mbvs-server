from .models import Event
from rest_framework import serializers
from subscriptions.models import Subscription

class EventSerializer(serializers.HyperlinkedModelSerializer):
    # subscriptions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Event
        fields = "__all__"