from rest_framework import serializers
from .models import AircraftType, AircraftAssembly
from part.serializers import PartSerializer
from personnel.serializers import TeamSerializer


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftType
        fields = ['name']

    def validate_name(self, value):
        if AircraftType.objects.filter(name=value).exists():
            raise serializers.ValidationError('Aircraft model already exists')
        return value


class AssemblyAircraftSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer()

    class Meta:
        model = AircraftAssembly
        fields = ['aircraft', 'parts', 'assembled_by']
