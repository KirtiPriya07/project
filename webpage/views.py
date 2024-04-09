from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Great! Your data is safe with us.')
            return redirect('home')
            
    else:
        form = UserRegisterForm()
    return render(request, 'webpage/index.html' , {'form' : form})

def home(request):
    return render(request,"webpage/home.html")
