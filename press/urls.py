from django.conf.urls import patterns, url

from press import views

urlpatterns = patterns('',
    url(r'^$', views.get_presses, name='press list'),
)