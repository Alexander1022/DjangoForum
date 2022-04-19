from django.test import TestCase
from forum.models import Post
from django.contrib.auth import get_user_model

class TestModels(TestCase):

    def setUp(self):
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

    def test_post_is_created(self):
        self.assertEquals(self.post.title, 'Post 1')
        self.assertEquals(self.post.content, 'Post 1 content')