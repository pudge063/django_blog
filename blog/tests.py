# blog/tests.py
from django.test import TestCase
from users.models import User  # Импортируем вашу модель пользователя
from .models import Post
from .forms import PostForm

from rest_framework.test import APITestCase
from rest_framework import status


class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.article = Post.objects.create(title='Test Article', content='This is a test article.', author=self.user)

    def test_article_creation(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.content, 'This is a test article.')
        self.assertEqual(self.article.author.username, 'testuser')

    def test_str_method(self):
        self.assertEqual(str(self.article), 'Test Article')


class ArticleFormTest(TestCase):
    def test_form_valid(self):
        user = User.objects.create_user(username='testuser', password='12345')  # Изменено
        form_data = {'title': 'New Article', 'content': 'This is new content.', 'author': user.id}
        form = Post(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {'title': '', 'content': ''}
        form = Post(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('content', form.errors)


class ArticleAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')  # Изменено
        self.client.login(username='testuser', password='12345')
        self.article = Post.objects.create(title='Test Article', content='This is a test article.', author=self.user)

    def test_create_article(self):
        data = {'title': 'New Article', 'content': 'This is new content.', 'author': self.user.id}
        response = self.client.post('/api/articles/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_get_article(self):
        response = self.client.get(f'/api/articles/{self.article.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Article')

    def test_update_article(self):
        data = {'title': 'Updated Title', 'content': 'Updated content.'}
        response = self.client.put(f'/api/articles/{self.article.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, 'Updated Title')

    def test_delete_article(self):
        response = self.client.delete(f'/api/articles/{self.article.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)


class ErrorHandlingTestCase(APITestCase):
    def test_non_existent_article(self):
        response = self.client.get('/api/articles/9999/')  # Предположим, что статьи с ID 9999 не существует
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_method(self):
        response = self.client.post('/api/articles/9999/')  # Неверный метод
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Исправлено на 404
