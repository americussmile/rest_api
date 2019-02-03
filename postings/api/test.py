from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from postings.models import BlogPost
# automated
# new/blank db
User = get_user_model()

class BlogPostTestCase(APITestCase):
    def setUp(self):
        user = User(username='testcfeuser', email='test@test.com')
        user.set_password('1234')
        user.save()
        blog_posts = BlogPost.objects.create(user=user, title ='New title', content='random content')

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = BlogPost.objects.count()
        self.assertEqual(post_count, 1)