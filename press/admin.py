from django.contrib import admin
from press.models import Press

# Register your models here.
class PressAdmin(admin.ModelAdmin):
	list_display = ('name','link','pub_date')
	fields = ('name','cover','description','link',)


admin.site.register(Press, PressAdmin)
