from django.db import models
from django.utils.timezone import now

# Create your models here.
class Number(models.Model):
    number = models.IntegerField()
    created = models.DateTimeField(default=now)
