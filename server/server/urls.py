from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/courses/', include('apps.courses.urls')),
    path('api/students/', include('apps.students.urls')),
]
