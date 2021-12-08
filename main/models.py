import datetime
from django.contrib.auth import get_user_model
import django.utils.timezone
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.

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


class Meeting(models.Model):
    TimeToMeet = (("1", "10:00"),
                  ("2", "11:00"),
                  ("3", "12:00"),
                  ("4", "13:00"),
                  ("5", "14:00"),
                  ("6", "15:00"),
                  ("7", "16:00"),
                  ("8", "17:00"),
                  ("9", "18:00"))

    MeetingMassage = (("1", "Масаж спини"),
                      ("2", "Масаж шиї"),
                      ("3", "Мануальна терапія"),
                      ("4", "Антицилюлітний масаж"))

    user = models.ForeignKey(User, null= True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    date = models.DateField(default=django.utils.timezone.now())
    massage = models.TextField(choices=MeetingMassage, default="1")
    time = models.TextField(choices=TimeToMeet, default="6")
    is_done = models.BooleanField(default=False)





