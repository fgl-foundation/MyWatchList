# Generated by Django 3.0.4 on 2020-04-03 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Profile', '0008_auto_20200126_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='film',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='serial',
        ),
        migrations.AddField(
            model_name='notifications',
            name='item_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_notifi', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='item_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
