from django.core.management.base import BaseCommand
from aircraft.models import AircraftType


class Command(BaseCommand):
    help = 'Initialize aircraft types'

    def handle(self, *args, **kwargs):
        '''Entrypoint for command.'''
        self.stdout.write('Initializing aircraft types ...')
        aircraft_types = [
            'TB2',
            'TB3',
            'AKINCI',
            'KIZILELMA',
        ]

        for aircraft_name in aircraft_types:
            AircraftType.objects.get_or_create(name=aircraft_name)

        self.stdout.write(self.style.SUCCESS(
            'Aircraft types initialized successfully'))
