from django.core.management.base import BaseCommand
from personnel.models import Team


class Command(BaseCommand):
    help = 'Initialize teams'

    def handle(self, *args, **kwargs):
        '''Entrypoint for command.'''
        self.stdout.write('Initializing teams ...')
        teams = [
            'Wing Team',
            'Fuselage Team',
            'Tail Team',
            'Avionics Team',
            'Assembly Team'
        ]

        for team in teams:
            Team.objects.get_or_create(name=team)

        self.stdout.write(self.style.SUCCESS(
            'Teams initialized successfully'))
