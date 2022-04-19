from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Topic(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        posts = Post.objects.filter(topic_id = self.id)
        for post in posts:
            post.delete()
        return super().delete(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    topic_id = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
      
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(default = timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.content