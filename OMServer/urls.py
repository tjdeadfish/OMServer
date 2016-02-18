from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OMServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tools/', include('tools.urls')),
    url(r'^accounts/login/$', 'tools.views.login'),
    url(r'^accounts/logout/$', 'tools.views.logout'),
    url(r'^accounts/changepassword/$', 'tools.views.changepassword'),
    url(r'^index/$', 'tools.views.index'),
)
