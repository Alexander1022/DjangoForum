from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Topic(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={'pk': self.pk})

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    topic_id = models.ForeignKey('Topic', on_delete = models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.topic_id is None:
            self.topic_id = self.topic_id
            self.save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})   