from django.urls import path, include
from . import views

urlpatterns = [
    path('getAllDevices/', views.get_all_data),
]