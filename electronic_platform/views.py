from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from electronic_platform.models import Product, Contact, Supplier
from electronic_platform.permissions import IsActiveStaff
from electronic_platform.serializers import (
    ProductSerializer,
    ContactSerializer,
    SupplierSerializer,
)
from electronic_platform.services import CountryFilter


class ProductViewSet(ModelViewSet):
    """CRUD для работы с продуктами"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveStaff,)


class ContactViewSet(ModelViewSet):
    """CRUD для работы с контактами"""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsActiveStaff,)


class SupplierViewSet(ModelViewSet):
    """CRUD для работы с поставщиками"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter
    permission_classes = (IsActiveStaff,)
