from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('ninjas', views.create_ninja),
    path('dojos', views.create_dojo),
    path('dojos/<int:dojo_id>/delete', views.delete_dojo),
]