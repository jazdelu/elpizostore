from django.shortcuts import render_to_response
from press.models import Press
from django.template import RequestContext
from django.http import Http404
# Create your views here.
def get_latest_press(request):
	p = ''
	try:
		l = Press.objects.all()
	except:
		raise Http404
	p = l[0]
	l = list(Press.objects.all())
	i = l.index(p)
	next_p = l[1]
	prev_p =''
	return render_to_response('press.html',{'p':p,'next_p':next_p,'prev_p':prev_p},context_instance=RequestContext(request))

def get_press_by_id(request,pid):
	p = ''
	try:
		p = Press.objects.get(id = pid)
	except:
		raise Http404
	l = list(Press.objects.all())
	i = l.index(p)
	next_p =''
	prev_p =''
	if len(l)>1:
		if (i == 0):
			next_p = l[i+1]
		elif (i == len(l)-1):
			prev_p = l[i-1]
		else:
			next_p = l[i+1]
			prev_p = l[i-1]
	else:
		pass
	return render_to_response('press.html',{'p':p,'next_p':next_p,'prev_p':prev_p }, context_instance=RequestContext(request))

