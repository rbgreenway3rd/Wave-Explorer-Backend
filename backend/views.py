
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Wave Explorer Home</h1><h2>Bryan Greenway rocks!!!</h2>')
