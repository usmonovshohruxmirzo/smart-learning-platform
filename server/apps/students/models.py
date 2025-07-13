from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    enrolled_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
       return f"{self.first_name} {self.last_name}"