from django.conf.urls import patterns, url

from press import views

urlpatterns = patterns('',
    url(r'^$', views.get_latest_press, name='get_latest_press'),
    url(r'^(?P<pid>\d+)/$', views.get_press_by_id, name='get_latest_press'),
)