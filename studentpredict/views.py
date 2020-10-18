from django.http import HttpResponse
from django.shortcuts import render

from .models import studentperformance
# Create your views here.
def studentpredict_view(request, *args, **kwargs):
	#context = {'object': studentperformance.objects.all()}
	#return HttpResponse("<h1>Django 版本!<h1>")
	obj = studentperformance.objects.all()
	context = {
		'object': obj
	}

	return render(request, "studentpredict/studentpredict.html", context)