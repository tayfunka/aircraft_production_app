# Generated by Django 4.2.19 on 2025-02-26 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0001_initial'),
        ('aircraft', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aircraft',
            new_name='AircraftType',
        ),
    ]
