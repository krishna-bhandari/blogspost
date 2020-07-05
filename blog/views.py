from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
	blog=Blog.objects
	return render(request, 'blog/allblog.html',{'blog':blog})

def detail(request,blog_id):
	blog_detail=get_object_or_404(Blog, pk=blog_id)
	return render(request,'blog/detail.html',{'blogs':blog_detail})
