from django.core.management.base import BaseCommand
from personnel.models import Personnel, User, Team


class Command(BaseCommand):
    help = 'Initialize personnel'

    def handle(self, *args, **kwargs):
        '''Entrypoint for command.'''
        self.stdout.write('Initializing personnel ...')

        users = [
            {'username': 'person_wing', 'password': 'Baykar.,12', 'team': 'Wing Team'},
            {'username': 'person_fuselage',
                'password': 'Baykar.,12', 'team': 'Fuselage Team'},
            {'username': 'person_tail', 'password': 'Baykar.,12', 'team': 'Tail Team'},
            {'username': 'person_avionics',
                'password': 'Baykar.,12', 'team': 'Avionics Team'},
            {'username': 'person_assembly',
                'password': 'Baykar.,12', 'team': 'Assembly Team'}
        ]

        for user_data in users:
            user, created = User.objects.get_or_create(
                username=user_data['username'])
            if created:
                user.set_password(user_data['password'])
                user.save()
                team = Team.objects.get(name=user_data['team'])
                Personnel.objects.create(user=user, team=team)

                self.stdout.write(self.style.SUCCESS(
                    f'User {user.username} created successfully'))

        self.stdout.write(self.style.SUCCESS(
            'Personnel initialized successfully'))
