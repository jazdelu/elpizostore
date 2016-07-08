from django.shortcuts import render_to_response
from shop.models import Shop
from django.template import RequestContext
# Create your views here.
def get_shops(request):
	shops = ''
	return render_to_response("shop.html",{'shops': shops},context_instance=RequestContext(request))