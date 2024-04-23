from rest_framework import routers
from .views import ProductAPIViewSet

router = routers.DefaultRouter()
router.register(
    "product",
    ProductAPIViewSet
)

urlpatterns = router.urls
