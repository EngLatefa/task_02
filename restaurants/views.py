from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def template(request):
	context = {"msg": "Hello World!"}
	return render(request, 'untitled.html', context)