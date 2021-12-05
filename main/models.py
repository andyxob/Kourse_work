from django.db import models
#from django.contrib.auth.models import User
from django.db.models import ForeignKey
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.forms import DateTimeField
from  django.utils.timezone import now

User = settings.AUTH_USER_MODEL
class Doctor(models.Model):
    name = models.CharField('Name', max_length=80)
    category = models.CharField('Category', max_length=40)
    bio = models.TextField('Bio', max_length=500)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class Result(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    #date = models.DateTimeField(null=True)
    time = models.TextField(default=None)
    massage = models.TextField(default=None)

    def __str__(self):
        return self.massage

