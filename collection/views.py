from django.shortcuts import render_to_response
from collection.models import Collection, Lookbook
from django.template import RequestContext

# Create your views here.

def get_cover_image(cid):
	url = ''
	try:
		i = Lookbook.objects.get(collection = cid, set_to_cover = True )
		url = i.image.url
	except:
		pass
	return url

def get_latest_collection(request):
	c = Collection.objects.all().order_by('-pub_date')
	c = c[0]

	return render_to_response('collection.html',{'c':c,'cover':get_cover_image(c.id) },context_instance=RequestContext(request))

def get_collection_by_id(request,collection_id):
	c=''
	try:
		c = Collection.objects.get(id = collection_id)
	except Collection.DoesNotExist:
		pass
	return render_to_response('collection.html',{'c':c,'cover':get_cover_image(c.id) },context_instance=RequestContext(request))


