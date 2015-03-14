from django.shortcuts import render_to_response
from press.models import Press
from django.template import RequestContext
from django.http import Http404
# Create your views here.
def get_latest_press(request):
	p = ''
	try:
		l = Press.objects.all().order_by('-pub_date')
	except:
		raise Http404
	return render_to_response('press.html',{'p':p},context_instance=RequestContext(request))

def get_press_by_id(request,pid):
	p = ''
	try:
		p = Press.objects.get(id = pid)
	except:
		raise Http404
	return render_to_response('press.html',{'p':p }, context_instance=RequestContext(request))

