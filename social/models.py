from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created:%Y-%m-%d %H-%M}): "
            f"{self.body}"
        )


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