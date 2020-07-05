from django.shortcuts import render
# from .models import Job
# import re


def home(request):
	# jobs=Job.objects
	# context = {'jobs': jobs}
	return render(request, 'jobs/home.html')



 