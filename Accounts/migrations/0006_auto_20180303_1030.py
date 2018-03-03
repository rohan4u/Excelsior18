# Generated by Django 2.0.2 on 2018-03-03 10:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20180303_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_active',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='roll_no',
            field=models.CharField(max_length=12),
        ),
    ]
