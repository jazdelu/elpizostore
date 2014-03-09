from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'elpizostore.views.home', name='home'),
    url(r'^about/$', 'elpizostore.views.about', name='about'),
    url(r'^contact/$', 'elpizostore.views.contact', name='contact'),
    url(r'^collection/', include('collection.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^press/', include('press.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


