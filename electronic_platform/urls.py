from rest_framework.routers import DefaultRouter

from electronic_platform.apps import ElectronicPlatformConfig
from electronic_platform.views import SupplierViewSet, ProductViewSet, ContactViewSet

app_name = ElectronicPlatformConfig.name

supplier_router = DefaultRouter()
supplier_router.register(r"supplier", SupplierViewSet, basename="supplier")

product_router = DefaultRouter()
product_router.register(r"product", ProductViewSet, basename="product")

contact_router = DefaultRouter()
contact_router.register(r"contact", ContactViewSet, basename="contact")


urlpatterns = [] + supplier_router.urls + product_router.urls + contact_router.urls
