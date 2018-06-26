from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.name_list, name='name_list'),
url(r'^name/(?P<pk>\d+)/$', views.name_detail, name='name_detail'),
url(r'^name/new/$', views.name_new, name='name_new'),
url(r'^name/(?P<pk>\d+)/edit/$', views.name_edit, name='name_edit'),
url(r'^drafts/$', views.name_draft_list, name='name_draft_list'),
url(r'^name/(?P<pk>\d+)/publish/$', views.name_publish, name='name_publish'),
url(r'^name/(?P<pk>\d+)/remove/$', views.name_remove, name='name_remove'),
url(r'^name/(?P<pk>\d+)/approve/$', views.name_approve, name='name_approve'),
]