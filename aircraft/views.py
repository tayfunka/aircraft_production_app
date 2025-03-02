from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework import generics
from .models import AircraftType, AircraftAssembly
from rest_framework.response import Response
from .serializers import AircraftSerializer, AssemblyAircraftSerializer
from rest_framework import status
from personnel.models import Personnel
from part.models import Part
from aircraft.models import AircraftType, AircraftAssembly
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import AssembleAircraftForm
from django.db import transaction
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape


class AssembleAircraftView(View):
    '''Assemble Aircraft Django View'''

    @method_decorator(login_required)
    def get(self, request):
        assemble_aircraft_form = AssembleAircraftForm()
        return render(request, 'aircraft/assemble_aircraft_form.html', {'assemble_aircraft_form': assemble_aircraft_form})

    @method_decorator(login_required)
    def post(self, request):
        assemble_aircraft_form = AssembleAircraftForm(request.POST)
        if assemble_aircraft_form.is_valid():
            try:
                personnel = Personnel.objects.get(user=request.user)

                if personnel.team.name != 'Assembly Team':
                    return render(request, 'aircraft/assemble_aircraft_form.html', {
                        'assemble_aircraft_form': assemble_aircraft_form,
                        'error': 'You do not have permission to assemble aircraft'
                    })

                aircraft_name = assemble_aircraft_form.cleaned_data['aircraft']
                aircraft = AircraftType.objects.get(name=aircraft_name)
                if not aircraft:
                    return render(request, 'aircraft/assemble_aircraft_form.html', {
                        'assemble_aircraft_form': assemble_aircraft_form,
                        'error': 'Aircraft not found'
                    })

                with transaction.atomic():
                    assembly = AircraftAssembly(
                        aircraft=aircraft, assembled_by=personnel.team)
                    assembly.save()
                    assembly.assemble_aircraft()
                return render(request, 'aircraft/assemble_aircraft_form.html', {
                    'assemble_aircraft_form': assemble_aircraft_form,
                    'message': f'{aircraft.name} assembled successfully'
                })
            except Exception as e:
                return render(request, 'aircraft/assemble_aircraft_form.html', {
                    'assemble_aircraft_form': assemble_aircraft_form,
                    'error': str(e)
                })
        return render(request, 'aircraft/assemble_aircraft_form.html', {'assemble_aircraft_form': assemble_aircraft_form})


class ListAircraftAssemblyView(View):
    '''List Aircraft Assembly Django View'''

    @method_decorator(login_required)
    def get(self, request):
        personnel = Personnel.objects.get(user=request.user)
        if personnel.team.name == 'Assembly Team':
            assemblies = AircraftAssembly.objects.all()
        else:
            assemblies = AircraftAssembly.objects.filter(
                assembled_by=personnel.team)
        return render(request, 'aircraft/list_assembly.html', {'assemblies': assemblies})


class CreateAircraftType(generics.CreateAPIView):
    queryset = AircraftType.objects.all()
    serializer_class = AircraftSerializer


class ListAircraftType(generics.ListAPIView):
    queryset = AircraftType.objects.all()
    serializer_class = AircraftSerializer


class ListAircraftAssembly(generics.ListAPIView):
    queryset = AircraftAssembly.objects.all()
    serializer_class = AssemblyAircraftSerializer

    def get_queryset(self):
        personnel = Personnel.objects.get(user=self.request.user)
        if personnel.team.name == 'Assembly Team':
            return AircraftAssembly.objects.all()
        return AircraftAssembly.objects.filter(assembled_by=personnel.team)


class AssembleAircraft(generics.GenericAPIView):
    '''Assemble an Aircraft'''
    queryset = AircraftAssembly.objects.all()
    serializer_class = AircraftSerializer

    def post(self, request):
        personnel = Personnel.objects.get(user=request.user)
        try:
            if personnel.team.name != 'Assembly Team':
                return Response({'error': 'Only Assembly team can assemble aircrafts'}, status=status.HTTP_403_FORBIDDEN)

            aircraft = AircraftType.objects.get(name=request.data['name'])
            if not aircraft:
                return Response({'error': 'Aircraft not found'}, status=status.HTTP_404_NOT_FOUND)

            parts = Part.objects.filter(aircraft=aircraft)
            if not parts:
                return Response({'error': f'No parts available for {aircraft.name}'}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                assembly = AircraftAssembly(
                    aircraft=aircraft, assembled_by=personnel.team)
                assembly.save()
                assembly.assemble_aircraft()

            return Response({'message': f'{aircraft.name} assembled successfully'}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AircraftAssemblyListViewDatatable(BaseDatatableView):

    model = AircraftAssembly
    columns = ['aircraft__name', 'assembled_by__name', 'parts']
    order_columns = ['aircraft__name', 'assembled_by__name', 'parts']

    def render_column(self, row, column):
        print('CHECK THIS PRINT IF I SEND REQUEST PROPERLY')
        if column == 'aircraft__name':
            return escape(row.aircraft.name)
        elif column == 'parts':
            return escape(', '.join([part.name for part in row.parts.all()]))
        elif column == 'assembled_by__name':
            return escape(row.assembled_by.name)
        else:
            return super().render_column(row, column)

    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        print('CHECK THIS PRINT IF I SEND REQUEST PROPERLY')
        json_data = []
        for item in qs:
            json_data.append([
                escape(item.aircraft.name),
                escape(item.assembled_by.name),
                escape(', '.join([part.name for part in item.parts.all()]))
            ])
        return json_data
