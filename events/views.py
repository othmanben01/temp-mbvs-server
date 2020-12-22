from rest_framework import viewsets
from .models import Event
from rest_framework import permissions
from .serializers import EventSerializer
from rest_framework import renderers


class EventViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # renderer_classes = [renderers.StaticHTMLRenderer]
    # permission_classes = [permissions.IsAuthenticated]