from django.db import models

# Create your models here.
class Press(models.Model):
	name = models.CharField(max_length = 128)
	description = models.TextField(blank = True)
	link = models.URLField(blank = True)
	pub_date = models.DateTimeField(auto_now_add = True,auto_now = True,null = True)

	class Meta:
		verbose_name='Press'
		verbose_name_plural='Press'

	def __unicode__(self):
		return self.name

	def get_preview(self):
		image = self.images.all().get(set_to_preview = True)
		return image.url

def upload_to(instance, filename):
	return 'press/%d/%s'%(instance.press.id,filename)

class Image(models.Model):
	image = models.ImageField(upload_to=upload_to)
	press =  models.ForeignKey(Press,related_name = 'images')
	text = models.TextField(blank = True)
	pub_date = models.DateTimeField(auto_now_add = True,auto_now = True,null = True)
	set_to_preview = models.BooleanField(verbose_name = 'Set this image to preview?')

	def __unicode__(self):
		return self.image.url

	def save(self, *args, **kwargs):
		if self.set_to_preview:
			try:
				l = Image.objects.get(set_to_preview = True, press = self.press.id)
				l.set_to_preview = False
				l.save()
			except:
				pass
		else:
			pass

		super(Image, self).save(*args, **kwargs)