from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()


from blog.models import Blog
from blog.sitemap import BlogSitemap
from collection.models import Collection
from collection.sitemap import CollectionSitemap

sitemaps = {
	'blog':BlogSitemap,
	'collection':CollectionSitemap,
}




urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'elpizostore.views.home', name='home'),
    url(r'^about/$', 'elpizostore.views.about', name='about'),
    url(r'^contact/$', 'elpizostore.views.contact', name='contact'),
    url(r'^collection/', include('collection.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^press/', include('press.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)