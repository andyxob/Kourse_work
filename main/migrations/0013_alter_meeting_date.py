# Generated by Django 3.2.9 on 2021-12-08 10:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211208_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 8, 10, 52, 31, 162324, tzinfo=utc)),
        ),
    ]
