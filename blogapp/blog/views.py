from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Progress",
            "image": "1.jpg",
            "is_active": True,
            "is_home": False,
            "description": "Today is very bad",
        },
        {
            "id": 2,
            "title": "Progress",
            "image": "1.jpg",
            "is_active": True,
            "is_home": True,
            "description": "Today is very bad",
        },
        {
            "id": 3,
            "title": "Progress",
            "image": "1.jpg",
            "is_active": False,
            "is_home": True,
            "description": "Today is very bad",
        }
    ]
}

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True)
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/blog-details.html", {
        "blog": blog
    })