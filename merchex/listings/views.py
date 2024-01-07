from django.http import HttpResponse
from django.shortcuts import render

# Creation de nos views
def hello(request):
	return HttpResponse('<h1>Hello Django!</h1>')
