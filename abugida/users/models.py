from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid

from sqlalchemy import null

# Create your models here.

class Profile(models.Model):
    """ Every user has a profile """
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        unique=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to = 'profiles/', default='user-default.png')
    github_account = models.CharField(max_length=200, blank=True, null=True)
    twitter_account = models.CharField(max_length=200, blank=True, null=True)
    linkedin_account = models.CharField(max_length=200, blank=200)
    personal_website = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)
