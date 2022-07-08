from rest_framework import viewsets
from .models import Role
from rest_framework import permissions
from .serializers import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    # permission_classes = [permissions.IsAuthenticated]