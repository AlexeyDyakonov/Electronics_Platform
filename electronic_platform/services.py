import django_filters
from django_filters.rest_framework import FilterSet

from electronic_platform.models import Supplier


class CountryFilter(FilterSet):
    """Фильтр контакта по стране"""

    country = django_filters.CharFilter(
        field_name="contact__country", lookup_expr="icontains"
    )

    class Meta:
        model = Supplier
        fields = ["country"]
