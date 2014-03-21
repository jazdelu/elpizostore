from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
# Create your models here.
class Press(models.Model):
	name = models.CharField(max_length = 128)
	cover = models.ImageField(upload_to='press/',default = '' )
	thumbnail_small = ImageSpecField(source='cover',
                                      processors=[ResizeToFit(100)],
                                      format='JPEG',
                                      options={'quality': 100})
	description = models.TextField(blank = True)
	link = models.URLField(blank = True)
	pub_date = models.DateTimeField(auto_now_add = True,auto_now = True,null = True)

	class Meta:
		verbose_name='Press'
		verbose_name_plural='Press'

	def image_tag(self):
		return u'<img src = "%s"/>' % self.thumbnail_small.url 
	image_tag.short_description = u'Thumb'
	image_tag.allow_tags = True

	def __unicode__(self):
		return self.name
