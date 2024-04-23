from rest_framework import routers
from .views import ImageAPIViewSet

router = routers.DefaultRouter()
router.register(
    "image",
    ImageAPIViewSet
)

urlpatterns = router.urls
