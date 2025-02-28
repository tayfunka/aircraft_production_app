# filepath: /Users/proxycode2/Desktop/tayfunka/aircraft_production_app/personnel/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Personnel, Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']


class PersonnelSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    team = serializers.CharField()

    class Meta:
        model = Personnel
        fields = ['user', 'team']

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        team_data = validated_data.pop('team')
        serializer = UserSerializer()
        user = serializer.create(validated_data=user_data)
        team = Team.objects.get(name=team_data)
        personnel = Personnel.objects.create(
            user=user, team=team, **validated_data)
        return personnel
