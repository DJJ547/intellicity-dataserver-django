from django.urls import path, include
from . import views

urlpatterns = [
    path('getAllData/', views.get_all_data),
    path('updateIncidents/', views.update_incidents),
    path('updateCongestions/', views.update_congestions),
]