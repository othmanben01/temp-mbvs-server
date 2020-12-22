from rest_framework import routers
from .views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

profiles_router = router