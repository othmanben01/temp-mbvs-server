from rest_framework import routers
from .views import SubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet)

subscriptions_router = router