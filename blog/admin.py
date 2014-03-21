from django.contrib import admin
from blog.models import Blog, Image, Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','get_category','pub_date_format')
	fields = ('title','category','content','image_preview','pub_date')

	def get_category(self,obj):
		return obj.category.name
	get_category.short_description = 'Category'

	def pub_date_format(self,obj):
		return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")
	pub_date_format.admin_order_field = 'pub_date'
	pub_date_format.short_description = u'Publish Date'

class ImageAdmin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)
	list_display = ('get_blog','image_tag','set_to_preview')
	list_filter = ('blog',)
	fields = ('image','image_tag','blog','set_to_preview')

	def get_blog(self,obj):
		return obj.blog.title
	get_blog.short_description = 'Blog'


admin.site.register(Blog,BlogAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Category)