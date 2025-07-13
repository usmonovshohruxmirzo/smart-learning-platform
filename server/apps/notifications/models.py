from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title