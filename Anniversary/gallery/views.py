from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
from gallery.models import pic
from django.utils.timezone import get_current_timezone, utc, get_default_timezone
import datetime

# Create your views here.
def index(request):
	pics = pic.objects.all().order_by("pic_time")
	return render(request, 'index.html', {
		'pics': pics,
		'settings': settings,
		})

def letter(request):
	return render(request, 'letter.html', {
		'settings': settings,
		})