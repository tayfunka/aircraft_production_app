# Generated by Django 4.2.19 on 2025-02-27 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0002_rename_stock_count_part_piece'),
        ('personnel', '0001_initial'),
        ('aircraft', '0002_rename_aircraft_aircrafttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AircraftAssembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aircraft.aircrafttype')),
                ('assembled_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel.team')),
                ('parts', models.ManyToManyField(to='part.part')),
            ],
        ),
    ]
