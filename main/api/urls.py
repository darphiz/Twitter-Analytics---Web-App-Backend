from django.urls import path
from . import views

urlpatterns = [
    path('get_threads_tweets/', views.get_thread_tweets, name='get_thread_tweets'),
    path('get_thread/', views.get_thread_from_tweets, name='get_thread_from_tweets'),
    path('get_questions/', views.get_questions_tweets, name='get_questions_tweets'),
    path('get_others/', views.get_others, name='get_others'),
]