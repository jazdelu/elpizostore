from django.contrib import admin
from shop.models import Shop
# Register your models here.


class ShopAdmin(admin.ModelAdmin):
	list_display = ('name','link',)
	fields = ('name','logo','link')


admin.site.register(Shop,ShopAdmin)