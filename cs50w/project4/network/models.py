from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True
    )

class Post(models.Model):
    creator = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete = models.CASCADE,
            related_name = "post")
    likes = models.IntegerField(default = 0)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
