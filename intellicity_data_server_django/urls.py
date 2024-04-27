from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_system.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('notification/', include('notifications.urls')),
]
