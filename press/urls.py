from django.conf.urls import patterns, url

from press import views

urlpatterns = patterns('',
    url(r'^$', views.get_latest_press, name='get_latest_press'),
)