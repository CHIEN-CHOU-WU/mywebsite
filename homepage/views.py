from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
	#context = {'object': studentperformance.objects.all()}
	#return HttpResponse("<h1>Django 版本!<h1>")

	return render(request, "homepage/index.html", {})