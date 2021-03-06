from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from postings.models import BlogPost
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER
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

    def test_get_list(self):
        data = {}
        url =  api_reverse('api-postings:post-listcreate')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_post_item(self):
        data = {'title': 'random', 'content':'even more random'}
        url =  api_reverse('api-postings:post-listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        blog_post = BlogPost.objects.first()
        data = {}
        url =  blog_post.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_update_item(self):
        blog_post = BlogPost.objects.first()
        data = {'title': 'random', 'content':'even more random'}
        url = blog_post.get_api_url()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print(response.data)

    def test_update_item_with_user(self):
        blog_post = BlogPost.objects.first()
        data = {'title': 'random', 'content': 'even more random'}
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)
        url = blog_post.get_api_url()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)


