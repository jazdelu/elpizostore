from django.contrib import admin
from collection.models import Collection, Lookbook, Background

# Register your models here.

class BackgroundInline(admin.TabularInline):
	model = Background
	extra = 1

class CollectionAdmin(admin.ModelAdmin):
	list_display = ('name','pub_date_format')
	fields = ('name','description','pub_date')
	inlines = [BackgroundInline,]
	def pub_date_format(self,obj):
		return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")
	pub_date_format.admin_order_field = 'pub_date'
	pub_date_format.short_description = u'Publish Date'



class LookbookAdmin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)
	list_display = ('get_collection','image_tag','weight','pub_date_format')
	list_filter = ('collection',)
	fields = ('collection','image','image_tag','text','weight')
	def pub_date_format(self,obj):
		return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")
	pub_date_format.admin_order_field = 'pub_date'
	pub_date_format.short_description = u'Publish Date'


	def get_collection(self,obj):
		return obj.collection.name

	get_collection.short_description = 'Collection'


admin.site.register(Collection,CollectionAdmin)
admin.site.register(Lookbook,LookbookAdmin)