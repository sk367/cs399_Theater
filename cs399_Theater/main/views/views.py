
from django.shortcuts import render
from main.models import Events
from main.models import Tickets
from main.models import Merch

def index(request):
  	return render(request, 'index.html')
def location(request):
	return render(request, 'location.html')
def merch(request):
	return render(request, 'merch.html', {'merchs': Merch.objects.order_by('price')})
def performances(request):
	return render(request, 'performances.html', {'events': Events.objects.order_by('date')})
def tickets(request):
    return render(request, 'tickets.html', {'tickets': Tickets.objects.order_by('date')})
def golden(request):
    return render(request, 'golden.html', {})
def sqeaky(request):
    return render(request, 'sqeaky.html', {})
def sheri(request):
    return render(request, 'sheri.html', {})
