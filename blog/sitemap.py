from django.contrib.sitemaps import Sitemap
from blog.models import Blog

class BlogSitemap(Sitemap):
	changefreq = 'monthly'
	priority = 0.5

	def items(self):
		return Blog.objects.all()

	def lastmode(self,obj):
		return obj.pub_date

	def location(self,obj):
		return '/blog/%s/' % obj.id