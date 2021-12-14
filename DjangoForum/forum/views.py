from django.shortcuts import render
from django.contrib import admin
# Create your views here.

def index(request): 
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    return render(request, 'signup.html')

def create_sub(request):
    return render(request, 'create_sub.html')

def create_post(request):
    return render(request, 'create_post.html')

def create_comment(request):
    return render(request, 'create_comment.html')

def all_subs(request):
    return render(request, 'all_subs.html')