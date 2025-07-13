from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationView

router = DefaultRouter()
router.register('', NotificationView)

urlpatterns = [
    path('', include(router.urls))
]