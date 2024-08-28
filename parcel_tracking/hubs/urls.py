from rest_framework.routers import SimpleRouter

from .api.views import HubListViewSet

app_name = "hubs"

router = SimpleRouter()
router.register("hubs", HubListViewSet, basename="hubs")


urlpatterns = router.urls
