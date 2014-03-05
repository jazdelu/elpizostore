from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
class Collection(models.Model):
	name = models.CharField(max_length = 128)
	description = models.TextField(blank = True)
	pub_date = models.DateTimeField(verbose_name='publish date',auto_now_add = True,auto_now = True)

	def __unicode__(self):
		return self.name

class Lookbook(models.Model):
	image = models.ImageField(upload_to='lookbook/')
	thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(320, 480)],
                                      format='JPEG',
                                      options={'quality': 100})
	collection = models.ForeignKey(Collection, related_name = 'lookbooks')
	text = models.TextField(blank = True)
	set_to_cover = models.BooleanField()
	pub_date = models.DateTimeField(verbose_name = 'publish date',auto_now_add = True,auto_now = True)

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
