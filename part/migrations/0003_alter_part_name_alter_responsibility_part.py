# Generated by Django 4.2.19 on 2025-02-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0002_rename_stock_count_part_piece'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='name',
            field=models.CharField(choices=[('Wing', 'Wing'), ('Fuselage', 'Fuselage'), ('Tail', 'Tail'), ('Avionics', 'Avionics')], max_length=100),
        ),
        migrations.AlterField(
            model_name='responsibility',
            name='part',
            field=models.CharField(choices=[('Wing', 'Wing'), ('Fuselage', 'Fuselage'), ('Tail', 'Tail'), ('Avionics', 'Avionics')], max_length=10),
        ),
    ]
