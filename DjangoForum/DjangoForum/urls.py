from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/login', views.login, name="login"),
    path('/logout', views.logout, name="logout"),
    path('/signup', views.signup, name="signup"),
    path('/create_sub', views.create_sub, name="create-sub"),
    path('/create_post', views.create_post, name="create-post"),
    path('/create_comment', views.create_comment, name="create-comment"),
    path('/all_subs', views.create_comment, name="create-comment"),
]
