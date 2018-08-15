from django.shortcuts import render, get_object_or_404
from .models import Blog

#function to get objects from blog app"""
def myblog(request):
    posts = Blog.objects
    return render(request, "blog/myblog.html", {'posts':posts})

#Function returning the primary key of all objects in job or displays a 404 error
def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk =blog_id)
    return render(request, 'blog/detail.html', {'blog':blog_detail})

