""" This is a signal module for executing
    an event based on another event triggered
"""
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

def createProfile(sender, instance, created, **kwargs):
    """ A Function that creates a profile when user is created """
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )

def deleteUser(sender, instance, **kwargs):
    """ A function that deletes a user when profile is deleted """
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)