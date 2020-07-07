from django.shortcuts import render,redirect
from .models import Job
# import re


def home(request):
	jobs=Job.objects
	context = {'jobs': jobs}
	return render(request, 'job/index.html',context)



def profile(request):
	return render(request, 'job/profile.html')

def add_job(request):
	if request.method=='POST':
		if request.POST['title'] and request.POST['summary']:
			new_job=Job()
			new_job.title=request.POST['title']
			new_job.summary=request.POST['summary']
			new_job.image=request.FILES['image']
			new_job.save()
			return redirect('home')
		else:
			return render(request, 'job/profile.html')
	else:
		return redirect('profile')