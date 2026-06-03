from django.urls import path, include
from first_app import views as blog_views

urlpatterns = [
    path('blogs/', include('first_app.urls')),
    path('surveys/', include('surveys_app.urls')),
    path('', include('users_app.urls')),
]
