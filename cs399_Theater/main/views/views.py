from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'index.html')

def location(request):
	return render(request, 'location.html')
def merch(request):
	return render(request, 'merch.html')
def performances(request):
	return render(request, 'performances.html')
def tickets(request):
	return render(request, 'tickets.html')