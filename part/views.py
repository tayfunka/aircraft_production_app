from rest_framework import generics, status, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Part, Responsibility
from personnel.models import Team, Personnel
from django.views import View
from django.shortcuts import render, redirect
from .serializers import PartSerializer
from .forms import PartForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated


class PartCreateView(generics.GenericAPIView):
    '''Create Part'''
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PartSerializer(data=request.data)
        if serializer.is_valid():
            personnel = Personnel.objects.get(user=request.user)
            serializer.validated_data['created_by'] = personnel.team

            data = self.validate(data=serializer.validated_data)
            part = Part.objects.create(**data)
            return Response(PartSerializer(part).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate(self, data):
        print(data)
        if not Responsibility.objects.filter(team=data['created_by'], part=data['name']).exists():
            raise ValidationError(
                f"{data['created_by'].name} is not responsible for producing {data['name'].name} parts.")
        return data


class PartListView(generics.ListAPIView):
    '''List Parts'''
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        personnel = Personnel.objects.get(user=self.request.user)
        return Part.objects.filter(created_by=personnel.team)


class PartDeleteView(generics.DestroyAPIView):
    '''Delete Part'''
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        personnel = Personnel.objects.get(user=self.request.user)
        if instance.created_by != personnel.team:
            raise ValidationError(
                "You do not have permission to delete this part.")
        instance.delete()


class PartCreate(View):
    '''Create Part with Django View'''

    @method_decorator(login_required)
    def get(self, request):
        part_form = PartForm()
        return render(request, 'part/part_form.html', {'part_form': part_form})

    @method_decorator(login_required)
    def post(self, request):
        part_form = PartForm(request.POST)
        if part_form.is_valid():
            part = part_form.save(commit=False)
            personnel = Personnel.objects.get(user=request.user)
            part.created_by = personnel.team

            try:
                self.validate(part)
                part.save()
                return redirect('part:part-list')
            except ValidationError as e:
                part_form.add_error(None, e.detail)

        return render(request, 'part/part_form.html', {'part_form': part_form})

    def validate(self, part):
        if not Responsibility.objects.filter(team=part.created_by, part=part.name).exists():
            raise ValidationError(
                f"{part.created_by.name} is not responsible for producing {part.name} parts.")


class PartList(View):
    '''List Parts with Django View'''
    @method_decorator(login_required)
    def get(self, request):
        parts = Part.objects.filter(
            created_by=Personnel.objects.get(user=request.user).team)
        for part in parts:
            if part.piece == 0:
                part.delete()
        return render(request, 'part/part_list.html', {'parts': parts})
