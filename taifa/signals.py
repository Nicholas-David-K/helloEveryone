from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


def createUserProfile(sender, instance, created, **kwargs):
    print('created: ', created)
    if created:
        Profile.objects.create(user=instance)


post_save.connect(createUserProfile, sender=User)