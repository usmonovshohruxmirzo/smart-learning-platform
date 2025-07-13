from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer

class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer