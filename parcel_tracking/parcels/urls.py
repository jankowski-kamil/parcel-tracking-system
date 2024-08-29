from rest_framework.routers import SimpleRouter
from parcel_tracking.parcels.api.views import ParcelAddressViewSet, ParcelViewSet, ParcelSizeViewSet

app_name = "parcels"

router = SimpleRouter()
router.register("parcel-address", ParcelAddressViewSet, basename="parcel-address")
router.register("parcels", ParcelViewSet, basename="parcels")
router.register("parcel-size", ParcelSizeViewSet, basename="parcel-size")


urlpatterns = router.urls
