from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePg, name= 'home'),
    path('signup/', views.signUp, name='signup'),
    path('signin/', views.signIn, name= 'signin'),
    path('logout/', views.logOut, name= 'logout'),
    path('post/<int:post_id>/', views.singlePost, name= 'single-post'),
    path('cart/<int:post_id>/', views.addToCart, name='cart')
   
]