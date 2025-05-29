from django.urls import path  
from .views import get_posts, get_post, create_post, update_post, delete_post

urlpatterns = [
    path('', get_posts, name='get_posts'),
    path('posts/<int:post_id>/', get_post, name='details_post'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:post_id>/update/', update_post, name='update_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),
]
