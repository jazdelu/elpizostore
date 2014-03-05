from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.get_blogs, name='blog list'),
    url(r'^(?P<blog_id>\d+)/$', views.get_blog_by_id, name='get_blog_by_id'),
)