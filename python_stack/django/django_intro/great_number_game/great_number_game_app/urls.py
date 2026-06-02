from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guess', views.guess, name='guess'),
    path('submit_winner', views.submit_winner, name='submit_winner'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
]
