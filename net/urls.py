from django.urls import path, include
from rest_framework.routers import DefaultRouter

from net.views import SupplierViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"supplier", SupplierViewSet, basename="supplier")
router.register(r"product", ProductViewSet, basename="product")

app_name = "net"
urlpatterns = [
    path("", include(router.urls)),
]
