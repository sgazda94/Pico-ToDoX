from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(
        User, related_name="tasks", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name