from django.contrib.auth.models import Group
from .models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]