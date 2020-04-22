from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='blog-home'),
    path('photo/', views.photo,name='blog-photo'),
    path('filmy/', views.films,name='blog-films'),
    path('home/', views.home,name='blog-home'),
    path('about/', views.about, name='blog-base'),

]
