from django.db import models
from uuid import uuid4


class ToDo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    used_id = models.CharField(max_length=300)
    complete = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField()
    level_of_task = models.IntegerField()
    task = models.CharField(max_length=300)