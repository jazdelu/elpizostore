from django.contrib import admin
from press.models import Press, Image

# Register your models here.
class PressAdmin(admin.ModelAdmin):
	list_display = ('name','link','pub_date')
	fields = ('name','description','link',)

class ImageAdmin(admin.ModelAdmin):
	list_display = ('get_press','image','set_to_preview')
	fields = ('press','image','set_to_preview','text',)

	def get_press(self,obj):
		return obj.press.name
	get_press.short_description = 'Press'

admin.site.register(Press, PressAdmin)
admin.site.register(Image, ImageAdmin)