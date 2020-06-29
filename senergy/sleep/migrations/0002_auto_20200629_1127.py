# Generated by Django 3.0.7 on 2020-06-29 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sleeprecord',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='sleeprecord',
            name='data',
            field=models.TextField(default='[]'),
        ),
    ]
