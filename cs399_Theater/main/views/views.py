
from django.shortcuts import render
from main.models import Events

def index(request):
  soonest_event = Events.objects.order_by('date')[0]
  context = {'soonest_event': soonest_event}
  return render(request, 'index.html', context)

def location(request):
	return render(request, 'location.html')
def merch(request):
	return render(request, 'merch.html')
def performances(request):
	return render(request, 'performances.html')
def tickets(request):
  soonest_event = Events.objects.order_by('date')[0:]
  context = {'soonest_event': soonest_event}
  return render(request, 'tickets.html', context)