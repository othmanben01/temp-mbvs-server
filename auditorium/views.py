from rest_framework import viewsets
from .models import Auditorium, Video
from rest_framework import permissions
from .serializers import AuditoriumSerializer, VideoSerializer

class AuditoriumViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    """
    API endpoint that allows auditoriums to be viewed or edited.
    """
    queryset = Auditorium.objects.all()
    serializer_class = AuditoriumSerializer



class VideoViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    """
    API endpoint that allows videos to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer