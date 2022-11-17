from django.db import models

class Tasks(models.Model):
    task = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
