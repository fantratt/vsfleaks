from django.conf.urls import patterns, url

from vsfleakssite import views

urlpatterns = patterns('',
    url(r'^report/$', views.report, name='report'),
    url(r'^report/result/$', views.result, name='result'),
)