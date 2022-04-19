from django.test import TestCase, Client
from django.urls import reverse
from forum.models import Post
from django.contrib.auth import get_user_model

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()

        UserModel = get_user_model()
        user = UserModel.objects.create_user('user1', password='user1pass12345')
        user.is_superuser = False
        user.is_staff = False
        user.save()

        self.post = Post.objects.create(
            title = 'Post 1',
            content = 'Post 1 content',
            author = user
        )
    
    def test_home_GET(self):
        response = self.client.get(reverse('forum-home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/home.html')

    def test_post_detail_GET(self):
        response = self.client.get(reverse('post-detail', args=[1]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/post_detail.html')



