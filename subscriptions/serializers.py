from .models import Subscription
from rest_framework import serializers


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"