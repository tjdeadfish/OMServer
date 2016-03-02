from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OMServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/tongji/', include('tongji.urls')),
    url(r'^accounts/login/$', 'tools.views.login'),
    url(r'^accounts/logout/$', 'tools.views.logout'),
    url(r'^accounts/changepassword/$', 'tools.views.changepassword'),
    url(r'^index/$', 'tools.views.index'),
    url(r'^index/deploy/', include('deploy.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
