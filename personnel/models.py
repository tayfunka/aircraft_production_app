from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    TEAM_TYPES = [
        ('Wing Team', 'Wing Team'),
        ('Fuselage Team', 'Fuselage Team'),
        ('Tail Team', 'Tail Team'),
        ('Avionics Team', 'Avionics Team'),
        ('Assembly Team', 'Assembly Team')]

    name = models.CharField(max_length=100, choices=TEAM_TYPES)

    def __str__(self):
        return self.name


class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
