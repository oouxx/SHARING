import django_filters
from .models import Software
from rest_framework import generics


class SoftwareFilter(django_filters.rest_framework.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_expr='lte')

    class Meta:
        model = Software
        fields = ['category', 'in_stock', 'min_price', 'max_price']
