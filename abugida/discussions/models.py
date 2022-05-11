from django.db import models
import uuid
from users.models import Profile
""" This module is where the database design of
    the web app 'discussions' implimented
"""

# Create your models here.


class Topic(models.Model):
    """ A class for topics since every discussion has a topic"""
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False)
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    """ Every discussion happens
        inside a room of a specific topic
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    host = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    """Inside Room we have quetions users can ask"""
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    querier = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body


class Answer(models.Model):
    """  For Every question asked there are answers given """
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    responder = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.body