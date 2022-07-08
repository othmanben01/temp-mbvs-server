from rest_framework import routers
from .views import AuditoriumViewSet, VideoViewSet

router = routers.DefaultRouter()
router.register(r'auditoriums', AuditoriumViewSet)

auditoriums_router = router



router_2 = routers.DefaultRouter()
router_2.register(r'videos', VideoViewSet)

videos_router = router_2