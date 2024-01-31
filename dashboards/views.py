from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, AddPostForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from .forms import AddUserForm, EditUserForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        "category_count": category_count,
        "blogs_count": blogs_count,
    }
    return render(request, 'dashboards/dashboard.html', context)

def categories(request):
    return render(request, 'dashboards/categories.html')

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboards/add_category.html', context)

def edit_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category':category
    }
    return render(request, 'dashboards/edit_category.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    category.delete()
    return redirect('categories')


# Posts

def posts(request):
    posts = Blog.objects.all()
    context = {
        "posts": posts, 
    }
    return render(request, 'dashboards/posts.html', context)


def add_posts(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.pk)
            form.save()
            return redirect('posts')
    form = AddPostForm()
    context = {
        "form": form,
    }
    return render(request, 'dashboards/add_posts.html', context)


def edit_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.pk)
            form.save()
            return redirect('posts')
    form = AddPostForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'dashboards/edit_posts.html', context)

def delete_posts(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blog.delete()
    return redirect('posts')


# Users

def users(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'dashboards/users.html', context)

def add_users(request):
    if request.method == "POST":
        form  = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUserForm()
    context = {
        "form": form,
    }
    return render(request, 'dashboards/add_users.html', context)


def edit_users(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('users')
        
    form = EditUserForm(instance=user)
    context = {
        "user": user,
        "form": form,
    }
    return render(request, 'dashboards/edit_users.html', context)

def delete_users(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')