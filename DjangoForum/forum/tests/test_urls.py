from django.test import SimpleTestCase
from django.urls import reverse, resolve
from forum.views import PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('forum-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_post_detail_url_is_resolved(self):        
        url = reverse('post-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_post_create_url_is_resolved(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_post_update_url_is_resolved(self):
        url = reverse('post-update', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)
        
    def test_post_delete_url_is_resolved(self):
        url = reverse('post-delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)