from django.db import models

# Create your models here.
class Shop(models.Model):
	name = models.CharField(max_length = 128,)
	logo = models.ImageField(upload_to= 'shop/')
	link = models.URLField()
	
	class Meta:
		verbose_name = "Shop"
		verbose_name_plural = "Shop"
		ordering = ['name',]

	def __unicode__(self):
		return self.name