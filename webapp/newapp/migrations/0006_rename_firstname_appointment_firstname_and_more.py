# Generated by Django 4.1.7 on 2023-03-17 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_rename_name_appointment_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='firstName',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='lastName',
            new_name='lastname',
        ),
    ]
