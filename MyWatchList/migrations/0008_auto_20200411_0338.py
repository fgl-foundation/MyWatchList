# Generated by Django 3.0.5 on 2020-04-11 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWatchList', '0007_auto_20200411_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='RUcert',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='UScert',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
