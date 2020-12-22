from rest_framework import viewsets
from .models import Subscription
from rest_framework import permissions
from .serializers import SubscriptionSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    """
    API endpoint that allows subscriptions to be viewed or edited.
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # permission_classes = [permissions.IsAuthenticated]