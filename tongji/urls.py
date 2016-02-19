from django.conf.urls import *
from tongji.views import server_info_display
from tongji.views import server_info_submit

urlpatterns = patterns('',
    url(r'^$', server_info_display),
    url(r'^submit/$', server_info_submit),
)
