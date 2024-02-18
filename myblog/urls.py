from django.urls import path
from . import views

urlpatterns = [
      path('', views.post_list, name='post_list'),
      path('post/<int:pk>/', views.post_detail, name='post_detail'),
      path('post/delete/<int:pk>/', views.deletePost, name='post_delete'),
      path('register/', views.signup, name='register'),
      path('post/new/', views.post_new, name='post_new'),

]
