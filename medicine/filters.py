from django.contrib.auth.models import User
import django_filters
from .models import medicine

class UserFilter(django_filters.FilterSet):
    medicine_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = medicine
        fields = ['medicine_name',]
