from django.shortcuts import  render, redirect
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def index(request): 
    return render(request, 'base.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user.username)

    else:
        return redirect('/login')
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return render(request, 'logout.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            user = authenticate(request, username=username, password=password1, password2=password2, email=email)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserRegistrationForm()
        
    context = { 'form': form }
    return render(request, 'signup.html', context)

def create_sub(request):
    return render(request, 'create_sub.html')

def create_post(request):
    return render(request, 'create_post.html')

def create_comment(request):
    return render(request, 'create_comment.html')

def all_subs(request):
    return render(request, 'all_subs.html')