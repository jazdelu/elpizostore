from django.contrib import admin
from press.models import Press

# Register your models here.
class PressAdmin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)
	list_display = ('name','link','image_tag','pub_date')
	fields = ('name','cover','image_tag','description','link',)

admin.site.register(Press, PressAdmin)
