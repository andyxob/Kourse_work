from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Doctor(models.Model):
    name = models.CharField('Name', max_length=40)
    surname = models.CharField('Surname', max_length=40)
    category = models.CharField('Category', max_length=40)
    bio = models.TextField('Bio', max_length=500)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


