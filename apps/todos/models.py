from django.db import models
from datetime import datetime
from user.models import CustomUser

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField("Date Created", default=datetime.now())

    def __str__(self):
        return self.title

