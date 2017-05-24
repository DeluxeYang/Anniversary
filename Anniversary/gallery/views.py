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
	n = datetime.datetime.now()
	pics = pic.objects.create(pic_title="1",pic_time=n.strftime('%Y-%m-%d %H:%M:%S'),pic_path="/",pic_text="a")
	#pt = pics.pic_time.astimezone(get_default_timezone())
	# get_default_timezone().normalize()
	# dt = datetime.datetime.strftime(pt, '%Y-%m-%d %H:%M:%S')
	
	return HttpResponse(pics.pic_time)