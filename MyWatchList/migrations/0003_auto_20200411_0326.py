# Generated by Django 3.0.5 on 2020-04-11 00:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWatchList', '0002_auto_20200411_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='RUcert',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='UScert',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 11, 3, 26, 20, 839138)),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_dateRU',
            field=models.DateField(default=datetime.datetime(2020, 4, 11, 3, 26, 20, 839138)),
        ),
    ]
