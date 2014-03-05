from django.shortcuts import render_to_response
from press.models import Press

# Create your views here.
def get_press_list(request):
	l = 