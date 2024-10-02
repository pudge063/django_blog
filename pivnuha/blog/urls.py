from django.urls import path
from .views import post_list, create_post, edit_post, delete_post
from .views import PostListAPIView, PostDetailAPIView, PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    
    # path('api/posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    # path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),

    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('api/posts/<int:pk>/edit/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),

]

