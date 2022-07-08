from rest_framework import routers
from .views import RegistrationAPI

router = routers.DefaultRouter()
router.register(r'registration', RegistrationAPI, basename='registration')

registration_router = router