from django.shortcuts import render, redirect
from blogs.models import Blog, About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:         
        form = RegistrationForm
    context = {
        'form':form,
    }
    return render(request,'register.html', context)


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("Authentication failed")
        else:
            print("Form is not valid")
            print(form.errors)
    
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')
