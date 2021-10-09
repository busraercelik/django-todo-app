from datetime import datetime

from django.db import models


class Todos(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=1000, blank=True)
    is_finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    # you can see todos by title on admins page
    def __str__(self):
        return self.title
