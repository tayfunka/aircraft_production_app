from django.db import models
from personnel.models import Team


class Part(models.Model):
    PART_TYPES = [
        ('Wing', 'Wing'),
        ('Fuselage', 'Fuselage'),
        ('Tail', 'Tail'),
        ('Avionics', 'Avionics')]

    name = models.CharField(max_length=100, choices=PART_TYPES)
    aircraft = models.ForeignKey(
        'aircraft.AircraftType', on_delete=models.CASCADE)
    piece = models.PositiveIntegerField(default=1)
    created_by = models.ForeignKey(Team, on_delete=models.CASCADE)

    def use_part(self):
        if self.piece > 0:
            self.piece -= 1
            self.save()
        else:
            self.delete()
            raise ValueError(f"No more {self.name} parts in stock.")

    def __str__(self):
        return f"{self.name} for {self.aircraft.name}"


class Responsibility(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    part = models.CharField(max_length=10, choices=Part.PART_TYPES)

    def __str__(self):
        return f"{self.team.name} - {self.part}"
