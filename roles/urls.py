from rest_framework import routers
from .views import RoleViewSet

router = routers.DefaultRouter()
router.register(r'roles', RoleViewSet)

roles_router = router