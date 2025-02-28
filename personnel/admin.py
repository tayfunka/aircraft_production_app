from django.contrib import admin
from .models import Personnel, Team
from part.models import Responsibility, Part
from aircraft.models import AircraftType, AircraftAssembly
# Register your models here.

admin.site.register(Personnel)
admin.site.register(Team)
admin.site.register(Responsibility)
admin.site.register(Part)
admin.site.register(AircraftType)
admin.site.register(AircraftAssembly)
