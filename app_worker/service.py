from django_filters import rest_framework as filters
from app_worker.models import Worker


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class WorkerFilter(filters.FilterSet):
    """Фильтрация представления о работниках"""
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    position = CharFilterInFilter(field_name='position', lookup_expr='in')
    hired_at = filters.RangeFilter()
    salary = filters.RangeFilter()
    chief = filters.NumberFilter()

    class Meta:
        model = Worker
        fields = ['name', 'position', 'hired_at', 'salary', 'chief']