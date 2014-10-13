from django.conf.urls import patterns, url

from vsfleakssite import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^tags/(?P<tag>\w+)/$', views.index, name='index'),
    url(r'^report/$', views.report, name='report'),
    url(r'^report/result/$', views.result, name='result'),
    url(r'^post/(?P<slug>[\w\-]+)/$', views.post, name='post'),
)