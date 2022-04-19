from django.test import TestCase
from forum.models import Post, Topic, Comment
from django.contrib.auth import get_user_model

class TestModels(TestCase):

    def setUp(self):
        UserModel = get_user_model()
        user = UserModel.objects.create_user('user1', password='user1pass12345')
        user.is_superuser = False
        user.is_staff = False
        user.save()

        self.topic = Topic.objects.create(
            title = 'Topic 1',
            description = 'Desc',
            author = user
        )

        self.post = Post.objects.create(
            title = 'Post 1',
            topic_id = self.topic,
            content = 'Post 1 content',
            author = user
        )

        self.comment = Comment.objects.create(
            author = user,
            post = self.post,
            content = 'Comment 1'
        )

    def test_post_is_created(self):
        self.assertEquals(self.post.title, 'Post 1')
        self.assertEquals(self.post.content, 'Post 1 content')

    def test_topic_is_created(self):
        self.assertEquals(self.topic.title, 'Topic 1')
        self.assertEquals(self.topic.description, 'Desc')
       
    def test_comment_is_created(self):
        self.assertEquals(self.comment.content, 'Comment 1')