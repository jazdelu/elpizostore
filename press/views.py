from django.shortcuts import render_to_response
from press.models import Press
from django.template import RequestContext
# Create your views here.
def get_presses(request):
	l = Press.objects.all().order_by('-pub_date')
	return render_to_response('press.html',{'l':l,},context_instance=RequestContext(request))
