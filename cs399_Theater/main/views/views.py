
from django.shortcuts import render
from main.models import Events
from main.models import Tickets

def index(request):
  	return render(request, 'index.html')
def location(request):
	return render(request, 'location.html')
def merch(request):
	return render(request, 'merch.html')
def performances(request):
	return render(request, 'performances.html', {'events': Events.objects.order_by('date')})
def tickets(request):
  return render(request, 'tickets.html', {'tickets': Tickets.objects.order_by('date')})
