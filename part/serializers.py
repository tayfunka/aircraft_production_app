

from rest_framework import serializers
from .models import Part, Responsibility


class PartSerializer(serializers.ModelSerializer):
    '''Part Serializer'''

    class Meta:
        model = Part
        fields = ['name', 'aircraft']
