from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    starttime = models.TimeField()
    endtime = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title