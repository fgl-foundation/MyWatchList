# Generated by Django 3.0.5 on 2020-04-11 00:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWatchList', '0004_auto_20200411_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_dateRU',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
