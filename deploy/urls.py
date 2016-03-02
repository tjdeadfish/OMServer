from django.conf.urls import *
from deploy import views


urlpatterns = patterns('',
    url(r'^$', views.service_list, name='service_list'),
    url(r'^new/$', views.service_create, name='service_new'),
    url(r'edit/(?P<pk>\d+)$', views.service_update, name='service_edit'),
    url(r'delete/(?P<pk>\d+)$', views.service_delete, name='service_delete'),
    url(r'^select/$', views.select_operate, name='service_install'),
    url(r'^shell_script/$', views.save_scripts, name='save_scripts'),
)