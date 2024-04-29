import django_filters
from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    description = django_filters.CharFilter(field_name="description", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ('name', 'description')