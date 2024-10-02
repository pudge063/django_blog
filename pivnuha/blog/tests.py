from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post
from .forms import PostForm
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

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



class ArticleAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()  # Используем APIClient
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Создание поста для тестов
        self.post = Post.objects.create(title='Test Title', content='Test Content', author=self.user)

    def test_create_article(self):
        response = self.client.post(reverse('post-list-create'), {'title': 'New Title', 'content': 'New Content'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_article(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_article(self):
        response = self.client.put(reverse('post-detail', kwargs={'pk': self.post.pk}), {'title': 'Updated Title', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_article(self):
        response = self.client.delete(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)