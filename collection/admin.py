from django.contrib import admin
from collection.models import Collection, Lookbook

# Register your models here.

class CollectionAdmin(admin.ModelAdmin):
	list_display = ('name','pub_date')
	fields = ('name','description','pub_date')

class LookbookAdmin(admin.ModelAdmin):
	list_display = ('get_collection','image','set_to_cover')
	fields = ('collection','image','set_to_cover','text',)

	def get_collection(self,obj):
		return obj.collection.name

	get_collection.short_description = 'Collection'


admin.site.register(Collection,CollectionAdmin)
admin.site.register(Lookbook,LookbookAdmin)