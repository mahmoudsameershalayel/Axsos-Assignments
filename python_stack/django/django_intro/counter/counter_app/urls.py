from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('increment_by_two', views.increment_by_two),
    path('increment_by_amount', views.increment_by_amount),
    path('destroy_session', views.destroy_session),
]