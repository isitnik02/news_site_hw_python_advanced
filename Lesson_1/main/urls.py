from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # главная страница
    path('contact/', views.contact, name='contact'),  # страница контактов
    path('content/', views.content, name='content'),  # страница контента
    path('user_profile/', views.user_profile, name='user_profile'),   # страница профиля пользователя
    path('news_page/', views.news_page, name='news_page'),  # страница новости
]
