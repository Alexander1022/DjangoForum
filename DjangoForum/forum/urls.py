from re import template
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (PostListView, PostDetailView, PostUpdateView, PostCreateView, PostDeleteView)

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name='post_detail.html'), name='post-detail'),
    path('post/new/', PostCreateView.as_view(template_name='post_form.html'), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # this has to be updated
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='post_confirm_delete.html'), name='post-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)