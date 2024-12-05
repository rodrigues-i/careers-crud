from django.db import models

class Career(models.Model):
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title
