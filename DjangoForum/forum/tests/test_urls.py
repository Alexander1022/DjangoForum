from django.test import SimpleTestCase
from django.urls import reverse, resolve
from forum.views import PostCreateView, PostDeleteView, PostDetailView, PostUpdateView, TopicListView, TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('forum-home')
        self.assertEquals(resolve(url).func.view_class, TopicListView)

    def test_post_detail_url_is_resolved(self):        
        url = reverse('post-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_post_create_url_is_resolved(self):
        url = reverse('post-create', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_post_update_url_is_resolved(self):
        url = reverse('post-update', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_post_delete_url_is_resolved(self):
        url = reverse('post-delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)
    
    def test_topic_detail_url_is_resolved(self):
        url = reverse('topic-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, TopicDetailView)

    def test_topic_create_url_is_resolved(self):
        url = reverse('topic-create')
        self.assertEquals(resolve(url).func.view_class, TopicCreateView)
    
    def test_topic_update_url_is_resolved(self):
        url = reverse('topic-update', args=[1])
        self.assertEquals(resolve(url).func.view_class, TopicUpdateView)

    def test_topic_delete_url_is_resolved(self):
        url = reverse('topic-delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, TopicDeleteView)