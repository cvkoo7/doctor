from django.db import models


# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name
