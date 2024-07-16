from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def post_save_created_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.create(user=instance)
            profile.save()
        except:
            UserProfile.objects.get_or_create(user=instance)


@receiver(pre_save, sender=User)
def pre_save_created_profile(sender, instance, **kwargs):
    print(instance.first_name, instance.last_name)