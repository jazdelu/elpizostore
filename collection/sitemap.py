from django.contrib.sitemaps import Sitemap
from collection.models import Collection

class CollectionSitemap(Sitemap):
	changefreq = 'monthly'
	priority = 0.5

	def items(self):
		return Collection.objects.all()

	def lastmode(self,obj):
		return obj.pub_date

	def location(self,obj):
		return '/collection/%s/' % obj.id