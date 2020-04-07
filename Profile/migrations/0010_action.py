# Generated by Django 3.0.4 on 2020-04-03 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Profile', '0009_auto_20200403_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('verb', models.CharField(max_length=255, null=True)),
                ('item_ct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_obj', to='contenttypes.ContentType')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.Profile')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]