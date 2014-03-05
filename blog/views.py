from django.shortcuts import render_to_response
from blog.models import Blog
from django.http import Http404
from django.template import RequestContext
# Create your views here.
def get_blogs(request):
	l = Blog.objects.all().order_by('-pub_date')
	return render_to_response('blog.html',{'l':l},context_instance=RequestContext(request))

def get_blog_by_id(request,blog_id):
	b = ''
	try:
		b = Blog.objects.get(id = blog_id)
	except Blog.DoesNotExist:
		raise Http404

	return render_to_response('blog_detail.html',{'b':b},context_instance=RequestContext(request))
