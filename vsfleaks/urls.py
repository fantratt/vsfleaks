from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('zinnia.urls', namespace='zinnia')),
    url(r'^report/', include('vsfleakssite.urls', namespace='vsfleaks')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
) 
