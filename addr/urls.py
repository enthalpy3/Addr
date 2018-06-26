from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.name_list, name='name_list'),
url(r'^name/(?P<pk>\d+)/$', views.name_detail, name='name_detail'),
url(r'^name/new/$', views.name_new, name='name_new'),
url(r'^name/(?P<pk>\d+)/edit/$', views.name_edit, name='name_edit'),
]