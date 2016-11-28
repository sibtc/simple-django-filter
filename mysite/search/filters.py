from django import forms
from django.contrib.auth.models import User, Group

import django_filters


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'year_joined', 'groups']
