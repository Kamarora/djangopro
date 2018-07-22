from myapp.models import *
import django_filters
from django import forms

class UserFilter(django_filters.FilterSet):
    work_exp = django_filters.CharFilter(lookup_expr='icontains')
    skills = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = UserProfile
        fields = ['name','work_exp','preferred_loc','skills', ]