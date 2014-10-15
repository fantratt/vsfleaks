from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('zinnia.urls', namespace='zinnia')),
    url(r'^leaks/', include('vsfleakssite.urls', namespace='vsfleaks')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
)
