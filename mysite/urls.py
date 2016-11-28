from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django_filters.views import FilterView

from mysite.search.filters import UserFilter


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^search/$', FilterView.as_view(filterset_class=UserFilter, template_name='search/user_list.html'), name='search'),
    url(r'^admin/', include(admin.site.urls)),
]
