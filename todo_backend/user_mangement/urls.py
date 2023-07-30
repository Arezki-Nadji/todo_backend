from rest_framework import routers
from user_mangement.views import MeViewSet

router = routers.DefaultRouter()
router.register('me',MeViewSet, basename='me')