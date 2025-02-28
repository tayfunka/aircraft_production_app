from django.core.management.base import BaseCommand
from part.models import Team, Responsibility


class Command(BaseCommand):
    help = 'Initialize responsibilities for teams'

    def handle(self, *args, **kwargs):
        '''Entrypoint for command.'''
        self.stdout.write('Initializing responsibilities ...')
        responsibilities = [
            {'team_name': 'Wing Team', 'part': 'Wing'},
            {'team_name': 'Fuselage Team', 'part': 'Fuselage'},
            {'team_name': 'Tail Team', 'part': 'Tail'},
            {'team_name': 'Avionics Team', 'part': 'Avionics'},
        ]

        for resp in responsibilities:
            team, created = Team.objects.get_or_create(name=resp['team_name'])
            Responsibility.objects.get_or_create(
                team=team, part=resp['part'])

        self.stdout.write(self.style.SUCCESS(
            'Responsibilities initialized successfully'))
