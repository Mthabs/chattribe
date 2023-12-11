from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post

class PostListViewTest(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='nido', password='ni@_Do1*')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_posts(self):
        # Create some posts in the database
        Post.objects.create(user=self.user, content='Test Post 3')
        Post.objects.create(user=self.user, content='Test Post 6')

        # Make a GET request to list the posts
        response = self.client.get('/api/posts/')

        # Check that the request was successful (status code 201)
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

        # Check that the correct number of posts is returned
        self.assertEqual(len(response.data), 2)
    
    def test_create_post_authenticated_user(self):
        # Log in the user
        self.client.login(username='nido', password='ni@_Do1*')

        # Make a POST request to create a post
        data = {'content': 'New Test Post'}
        response = self.client.post('/api/posts/', data)


        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the request was successful (status code 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the post was created in the database
        self.assertEqual(Post.objects.count(), 1)

    def test_create_post_unauthenticated_user(self):
        # Log out the user (if logged in)
        self.client.logout()

        # Make a POST request to create a post
        data = {'content': 'New Test Post'}
        response = self.client.post('/api/posts/', data)

        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the request is unsuccessful for unauthenticated user (status code 403)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Check that no post was created in the database
        self.assertEqual(Post.objects.count(), 0)