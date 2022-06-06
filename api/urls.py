from django.urls import path, include
from . import views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    path('', (views.index), name='api-home'),
    path('posts/', (views.getPosts), name='api-home'),
    path('posts/<int:post_id>', (views.getPost), name='single-api'),
    path('posts/create/', (views.createPost), name='api-create'),
    path('posts/update/<int:post_id>', (views.updatePost), name='api-update'),
    path('posts/delete/<int:post_id>', (views.deletePost), name='api-delete'),
    
    path('login/', (views.apiLogin), name = "api-login"),
    path('signup/', (views.apiSignUp), name = "api-signup"),
]
