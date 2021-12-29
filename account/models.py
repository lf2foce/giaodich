from django.db import models

# Create your models here.
# đang test

from django.db import models
from django.contrib.auth.models import User


# đoạn này để auto update các trường còn lại
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    # note = 'iron', 'silver, 'gold', 'platinum', 'diamond', 'master', 'grandmaster', 'challenger'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=250, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                       blank=True)
    cash = models.DecimalField(max_digits=15, decimal_places=3, default=100000)
    borrower_level = models.CharField(max_length=255, default='iron')

    def __str__(self):
        return f'Profile for user {self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()