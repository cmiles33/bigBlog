from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class ArtPost(models.Model):
    upload = models.FileField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


