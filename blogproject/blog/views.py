from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':'Osho',
        'title':'Blog Post',
        'content':' First post content',
        'date_posted':'Aug 27 2026'
    },
    {
        'author':'jk krishnmurthy',
        'title':'Blog Post 2',
        'content':'Second  post content',
        'date_posted':'Aug 2 2026'
    }
]

def home(request):
    context ={
        'posts':posts
    }
    return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})
