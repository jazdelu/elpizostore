from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,ResizeToFit
# Create your models here.
class Collection(models.Model):
	name = models.CharField(max_length = 128)
	description = models.TextField(blank = True)
	pub_date = models.DateTimeField(verbose_name='publish date')

	class Meta:
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.name

class Lookbook(models.Model):
	image = models.ImageField(upload_to='lookbook/')
	thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(320, 480)],
                                      format='JPEG',
                                      options={'quality': 100})
	thumbnail_small = ImageSpecField(source='image',
                                      processors=[ResizeToFit(50)],
                                      format='JPEG',
                                      options={'quality': 100})
	collection = models.ForeignKey(Collection, related_name = 'lookbooks')
	text = models.TextField(blank = True)
	set_to_cover = models.BooleanField(default= False)
	weight = models.IntegerField(verbose_name = 'order',default = 1,help_text = 'Numbers only .The lookbook is ordered by ascending order field and ascending publish datetime. Order has higher priority.')
	pub_date = models.DateTimeField(verbose_name = 'publish date',auto_now_add = True,auto_now = True)

	class Meta:
		ordering = ['-collection','weight','-pub_date',]

	def image_tag(self):
		return u'<img src = "%s"/>' % self.thumbnail_small.url 
	image_tag.short_description = u'Thumb'
	image_tag.allow_tags = True

	def save(self,*args, **kwargs):
		if self.set_to_cover:
			try:
				l = Lookbook.objects.get(set_to_cover = True, collection = self.collection)
				l.set_to_cover = False
				l.save()
			except:
				pass
		else:
			pass

		super(Lookbook, self).save(*args, **kwargs)
