from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
class Press(models.Model):
	name = models.CharField(max_length = 128)
	cover = models.ImageField(upload_to='press/',default = '' )
	description = models.TextField(blank = True)
	link = models.URLField(blank = True)
	pub_date = models.DateTimeField(auto_now_add = True,auto_now = True,null = True)

	class Meta:
		verbose_name='Press'
		verbose_name_plural='Press'

	def __unicode__(self):
		return self.name
