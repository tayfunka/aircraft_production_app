

from django import forms
from .models import AircraftAssembly, AircraftType


class AssembleAircraftForm(forms.Form):
    aircraft = forms.ModelChoiceField(
        queryset=AircraftType.objects.all(), label="Select Aircraft")

    class Meta:
        model = AircraftAssembly
        fields = ['aircraft', 'parts', 'assembled_by']
