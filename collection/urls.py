from django.conf.urls import patterns, url

from collection import views

urlpatterns = patterns('',
    url(r'^$', views.get_latest_collection, name='latest'),
    url(r'^(?P<collection_id>\d+)/$', views.get_collection_by_id, name='get_collection_by_id'),
)