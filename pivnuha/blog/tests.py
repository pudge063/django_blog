from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post
from .forms import PostForm

User = get_user_model()


class ArticleFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_form_valid(self):
        form_data = {'title': 'New Article', 'content': 'This is new content.'}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {'title': '', 'content': ''}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('content', form.errors)



class ArticleAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='studentq', password='r22rkfss')
        self.client.login(username='studentq', password='r22rkfss')
        self.post = Post.objects.create(title='Test Article', content='This is a test article.', author=self.user)

    def test_create_article(self):
        data = {'title': 'New Article', 'content': 'This is new content.'}
        response = self.client.post(reverse('post-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_get_article(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Article')

    def test_update_article(self):
        data = {'title': 'Updated Title', 'content': 'Updated content.'}
        response = self.client.put(reverse('post-retrieve-update-destroy', kwargs={'pk': self.post.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_delete_article(self):
        response = self.client.delete(reverse('post-retrieve-update-destroy', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
