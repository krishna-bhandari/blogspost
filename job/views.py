from django.shortcuts import render
from .models import Job
# import re


def home(request):
	jobs=Job.objects
	context = {'jobs': jobs}
	return render(request, 'job/index.html',context)



def profile(request):
	
	return render(request, 'job/profile.html')