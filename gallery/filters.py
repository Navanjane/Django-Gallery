import django_filters
from django_filters import CharFilter

from .models import *

class Filter(django_filters.FilterSet):
    paint_name = CharFilter(field_name='paint_name', lookup_expr='icontains')

    class Meta:
        model = Paint
        fields = ['category']

