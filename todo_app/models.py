from django.db import models

# Create your models here.

class task(models.Model):
    tasks = models.TextField( max_length=200, blank=False)

    def __str__(self):
        return self.tasks

    