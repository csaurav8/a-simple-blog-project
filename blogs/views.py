from django.shortcuts import render, get_object_or_404 
from .models import Blog, Category
from django.db.models import Q


# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status = "Published", category = category_id)
    category = get_object_or_404(Category, pk = category_id)
    context ={
        "posts": posts,
        "category": category,
    }

    return render(request, 'posts_by_category.html', context)

def blog(request, slug):
    post = get_object_or_404(Blog, slug=slug, status = "Published")
    context = {
        "post": post,
    }
    return render(request, "single_blog.html", context)

def search(request):
    keyword = request.GET.get("keyword")
    posts = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains =keyword), status="Published") 
    context = {
        "posts": posts,
        "keyword": keyword,
    }
    return render(request, "search.html", context)