from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Lee',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Han',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

# Create your views here.
def index(request):
    return render(request, 'leeblog/index.html')

def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'leeblog/home.html', context)

def about(request):
    return render(request, 'leeblog/about.html', {'title': 'About'})
