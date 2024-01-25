from django.shortcuts import render
from blogs.models import Blog, About

def home(request):
    featured = Blog.objects.filter(is_featured = True, status = "Published").order_by("-created_at")
    not_featured = Blog.objects.filter(is_featured = False, status = "Published")
    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        "featured": featured,
        "not_featured": not_featured,
    }
    return render(request, 'home.html', context)

