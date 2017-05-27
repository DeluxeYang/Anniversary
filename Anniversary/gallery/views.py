from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
from gallery.models import pic
import gallery.models
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
    letter_latest = gallery.models.letter.objects.all().latest('letter_time')
    text = letter_latest.letter_text.split('\n')
    letter_from = letter_latest.letter_from.split('\n')
    return render(request, 'letter.html', {
        'letter':letter_latest,
        'text':text,
        'letter_from':letter_from,
        'settings': settings,
        })