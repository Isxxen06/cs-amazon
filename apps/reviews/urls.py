from rest_framework import routers
from .views import CategoryAPIViewSet

router = routers.DefaultRouter()
router.register(
    "reviews",
    CategoryAPIViewSet
)

urlpatterns = router.urls