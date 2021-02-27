from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import logout, authenticate
# Create your views here.

def home(request):
    if request.POST:
        try: 
            if request.POST["Logout"]:
                logout(request)
        except:
            pass
        
        
    return render(request, 'base/home.html')


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {"form":form})
    

def comment(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        if request.POST:
            form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            

    context= {    
        'tasks': tasks,
        'form': form
    }
    return render(request, 'comments/comment.html', context)