from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post

class PostListViewTest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='nido', password='ni@_Do1*')
        self.client = APIClient()
        self.client.force_authenticate(user=self.owner)

    def test_list_posts(self):
        Post.objects.create(owner=self.owner, content='Test Post 3')
        Post.objects.create(owner=self.owner, content='Test Post 6')

        # Make a GET request to list the posts
        response = self.client.get('/api/posts/')

        # Check that the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

        # Check that the correct number of posts is returned
        self.assertEqual(len(response.data), 2)
    
    def test_create_post_authenticated_owner(self):
        self.client.login(username='nido', password='ni@_Do1*')

        # Make a POST request to create a post
        data = {'content': 'New Test Post'}
        response = self.client.post('/api/posts/', data)

        # Check that the request was successful (status code 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the post was created in the database
        self.assertEqual(Post.objects.count(), 1)

    def test_create_post_unauthenticated_owner(self):
        self.client.logout()

        # Make a POST request to create a post
        data = {'content': 'New Test Post'}
        response = self.client.post('/api/posts/', data)

        # Check that the request is unsuccessful for unauthenticated owner (status code 403)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Check that no post was created in the database
        self.assertEqual(Post.objects.count(), 0)

class PostDetailViewTest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='nido', password='ni@_Do1*')
        self.post = Post.objects.create(owner=self.owner, content='Test Post')
        self.client = APIClient()
        self.client.force_authenticate(user=self.owner)

    def test_retrieve_post_valid_id(self):
        # Make a GET request to retrieve the post with a valid ID
        response = self.client.get(f'/api/posts/{self.post.id}/')

        # Check that the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the correct post data is returned
        self.assertEqual(response.data['content'], 'Test Post')
        # Check that the owner is the owner of the retrieved post
        self.assertEqual(response.data['owner'], 'nido')
        
    def test_retrieve_post_invalid_id(self):
        # Make a GET request to retrieve a post with an invalid ID
        response = self.client.get('/api/posts/999/')

        # Check that the request is unsuccessful for an invalid ID (status code 404)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_post_owner(self):                                                
        self.client.login(username='nido', password='ni@_Do1*')

        # Make a PUT request to update the post owned by the owner
        data = {'content': 'Updated Test Post'}
        response = self.client.put(f'/api/posts/{self.post.id}/', data)

        # Check that the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the post was updated in the database
        self.post.refresh_from_db()
        self.assertEqual(self.post.content, 'Updated Test Post')

    def test_update_post_non_owner(self):
        other_owner = User.objects.create_user(username='Sne', password='nhl@_Aka1*')

        # Authenticate the client with the other owner
        self.client.force_authenticate(user=other_owner)

        # Make a PUT request to update the post not owned by the owner
        data = {'content': 'Attempted Update'}

        # Add print statements to check the owner before and after the update
        print(f"Before Update - Owner: {other_owner.username}")
        response = self.client.put(f'/api/posts/{self.post.id}/', data)
        print(f"After Update - Owner: {other_owner.username}")

        # Check that the request is unsuccessful for a non-owner (status code 403)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Check that the post was not updated in the database
        self.post.refresh_from_db()
        self.assertEqual(self.post.content, 'Test Post')