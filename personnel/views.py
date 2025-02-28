from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Personnel, Team
from django.views import View
from django.shortcuts import render, redirect
from .serializers import PersonnelSerializer, TeamSerializer, UserSerializer
from .forms import UserForm, PersonnelForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PersonnelCreateView(generics.CreateAPIView):
    '''Create Personnel'''
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer


class TeamCreateView(generics.CreateAPIView):
    '''Create Team'''
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PersonnelCreate(View):
    '''Create Personnel with Django View'''

    def get(self, request):
        user_form = UserForm()
        personnel_form = PersonnelForm()
        return render(request, 'personnel/personnel_form.html', {'user_form': user_form, 'personnel_form': personnel_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        personnel_form = PersonnelForm(request.POST)
        if user_form.is_valid() and personnel_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            personnel = personnel_form.save(commit=False)
            personnel.user = user
            personnel.save()
            return redirect('personnel:home')
        return render(request, 'personnel/personnel_form.html', {'user_form': user_form, 'personnel_form': personnel_form})


class AuthenticateView(generics.GenericAPIView):
    '''Authenticate View'''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class Person(View):
    '''Person View'''

    @method_decorator(login_required)
    def get(self, request):
        person = Personnel.objects.get(user=request.user)
        return render(request, 'personnel/person.html', {'person': person})


class HomeView(View):
    '''Home View'''

    @method_decorator(login_required)
    def get(self, request):
        personnel = Personnel.objects.filter()
        return render(request, 'personnel/home.html')


class LoginView(View):
    '''Login View'''

    def get(self, request):
        return render(request, 'personnel/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('personnel:person')
        else:
            return HttpResponse('Invalid login')


class LogoutView(View):
    '''Logout View'''

    def get(self, request):
        logout(request)
        return redirect('personnel:login')
