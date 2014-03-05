from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
IMAGE_PREVIEW_CHOICES = (
		('h','horizontal'),
		('v','verticle'),
	)


class Category(models.Model):
	name = models.CharField(max_length = 128)

	def __unicode__(self):
		return self.name

class Blog(models.Model):

	title = models.CharField(max_length = 120)
	category = models.ForeignKey(Category)
	content = models.TextField(blank = True)
	pub_date = models.DateTimeField()
	image_preview = models.CharField(max_length= '128', choices = IMAGE_PREVIEW_CHOICES)

	def __unicode__(self):
		return self.title

	def get_preview_images(self):
		p = self.images.filter(set_to_preview = True)
		return p


def upload_to(instance, filename):
	return 'blog/%d/%s'%(instance.blog.id,filename)

class Image(models.Model):
	image = models.ImageField(upload_to=upload_to)
	thumbnail_h = ImageSpecField(source='image',
                                      processors=[ResizeToFill(160, 120)],
                                      format='JPEG',
                                      options={'quality': 80})
	thumbnail_v = ImageSpecField(source='image',
                                      processors=[ResizeToFill(120, 180)],
                                      format='JPEG',
                                      options={'quality': 100})

	blog =  models.ForeignKey(Blog,related_name = 'images')
	pub_date = models.DateTimeField(auto_now_add = True)
	set_to_preview = models.BooleanField()

	def __unicode__(self):
		return self.image.url