from django.db import models
from part.models import Part
from personnel.models import Team
from django.core.exceptions import ValidationError


class AircraftType(models.Model):
    AIRCRAFT_TYPES = [
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'AKINCI'),
        ('KIZILELMA', 'KIZILELMA'),
    ]

    name = models.CharField(max_length=100, choices=AIRCRAFT_TYPES)

    def __str__(self):
        return self.name


class AircraftAssembly(models.Model):
    aircraft = models.ForeignKey(AircraftType, on_delete=models.CASCADE)
    parts = models.ManyToManyField(Part)
    assembled_by = models.ForeignKey(Team, on_delete=models.CASCADE)

    def assemble_aircraft(self):
        required_parts = ['Wing', 'Fuselage', 'Tail', 'Avionics']
        existing_parts = []
        missing_parts = []
        for part_type in required_parts:
            part = Part.objects.filter(
                aircraft=self.aircraft, name=part_type).first()
            if not part:
                missing_parts.append(part_type)
            else:
                existing_parts.append(part)
        if missing_parts:
            raise ValueError(
                f"Missing parts: {', '.join(missing_parts)} for {self.aircraft.name}")

        for part in existing_parts:
            part.use_part()
            self.parts.add(part)
            self.save()

    def clean(self):
        for part in self.parts.all():
            if part.aircraft != self.aircraft:
                raise ValidationError(
                    f"Part {part.name} does not belong to the aircraft model {self.aircraft.name}")

    def __str__(self):
        return f"{self.aircraft.name} assembled by {self.assembled_by.name}"
