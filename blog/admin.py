from django.contrib import admin
from blog.models import Blog, Image, Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','get_category','pub_date')
	fields = ('title','category','content','image_preview','pub_date')

	def get_category(self,obj):
		return obj.category.name

	get_category.short_description = 'Category'

class ImageAdmin(admin.ModelAdmin):
	list_display = ('get_blog','image','set_to_preview')
	fields = ('image','blog','set_to_preview')

	def get_blog(self,obj):
		return obj.blog.title

	get_blog.short_description = 'Blog'

admin.site.register(Blog,BlogAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Category)