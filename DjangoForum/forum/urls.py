from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import TopicListView, TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView
from . import views

urlpatterns = [
    path('', TopicListView.as_view(), name = 'forum-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('topic/<int:pk>/post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name = 'topic-detail'),
    path('topic/new/', TopicCreateView.as_view(), name = 'topic-create'),
    path('topic/<int:pk>/update/', TopicUpdateView.as_view(), name = 'topic-update'),
    path('topic/<int:pk>/delete/', TopicDeleteView.as_view(), name = 'topic-delete'),
]