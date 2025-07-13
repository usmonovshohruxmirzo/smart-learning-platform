from django.db import models

class Student(models.Model):
    name: str = models.CharField(max_length=100)
    email: str = models.EmailField(unique=True)
    enrolled_date: str = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name