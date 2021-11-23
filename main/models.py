from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Doctor(models.Model):
    name = models.CharField('Name', max_length=40)
    surname = models.CharField('Surname', max_length=40)
    category = models.CharField('Category', max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created,  **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
