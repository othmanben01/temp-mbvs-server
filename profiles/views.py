from rest_framework import viewsets
from .models import Profile
from rest_framework import permissions
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    """
    API endpoint that allows profiles to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]