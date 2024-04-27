from django.urls import path, include
from . import views

urlpatterns = [
    path('getNotifications/', views.get_all_notifications),
]