# Generated by Django 2.0.2 on 2018-03-08 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0012_event_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='group_event',
        ),
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
