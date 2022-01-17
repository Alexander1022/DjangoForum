from django.shortcuts import  render, redirect
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Post
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def index(request): 
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})

def create_sub(request):
    return render(request, 'create_sub.html')

def create_post(request):
    return render(request, 'create_post.html')

def create_comment(request):
    return render(request, 'create_comment.html')

def all_subs(request):
    return render(request, 'all_subs.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)