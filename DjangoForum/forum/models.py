from os import defpath
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    followers = models.BigAutoField(editable=True, default=0)
    posts = models.BigAutoField(editable=True, default=0)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=150, editable=True)
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=300, editable=True)
    by_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, editable=True)
    desc = models.CharField(max_length=150, unique=False, editable=True)
    posts = models.BigAutoField(default=0)
    users_sub = models.BigAutoField(default=0)
