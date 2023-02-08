from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='followed_by')
    last_updated = models.DateTimeField(User, auto_now=True)
    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([user_profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)