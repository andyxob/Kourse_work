# Generated by Django 3.2.9 on 2021-12-08 10:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_remove_result_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2021, 12, 8))),
                ('time', models.TextField(choices=[('1', '10:00'), ('2', '11:00'), ('3', '12:00'), ('4', '13:00'), ('5', '14:00'), ('6', '15:00'), ('7', '16:00'), ('8', '17:00'), ('9', '18:00')])),
                ('massage', models.TextField(choices=[('1', 'Масаж спини'), ('2', 'Масаж шиї'), ('3', 'Мануальна терапія'), ('4', 'Антицилюлітний масаж')])),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.doctor')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
