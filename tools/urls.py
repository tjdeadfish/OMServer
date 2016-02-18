from django.conf.urls import *
from tools.views import DeviceTongJi
from tools.views import DeviceDisplay
urlpatterns = patterns('',
    url(r'device_submit/', DeviceTongJi),
    url(r'device_display', DeviceDisplay),
)
