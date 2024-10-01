from django.urls import path
from .views import post_list, create_post, edit_post, delete_post

urlpatterns = [
    path('', post_list, name='post_list'),  # Доступна всем
    path('create/', create_post, name='create_post'),  # Доступна только авторизованным
    path('edit/<int:post_id>/', edit_post, name='edit_post'),  # Редактирование поста
    path('delete/<int:post_id>/', delete_post, name='delete_post'),  # Удаление поста
]
