from django.db import models

class Review(models.Model):
    review = models.CharField(max_length=1000)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1)
    
    def __str__(self):
        return self.review