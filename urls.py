# face_recognition_attendance/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('face_recognition_attendance/', include('attendance.urls')),
]
