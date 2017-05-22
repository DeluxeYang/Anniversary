from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
from gallery.models import pic
# Create your views here.
def index(request):
	pics = pic.objects.all().order_by("pic_time")
	return render(request, 'index.html', {
		'pics': pics,
		'settings': settings,
		})