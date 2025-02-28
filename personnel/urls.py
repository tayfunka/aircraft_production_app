from django.urls import path
from . import views

app_name = 'personnel'

urlpatterns = [
    path('api/personnel-create/', views.PersonnelCreateView.as_view(),
         name='personnel-create-api'),
    path('api/personnel-authenticate/', views.AuthenticateView.as_view(),
         name='personnel-authenticate-api'),
    path('personnel-create/', views.PersonnelCreate.as_view(),
         name='personnel-create'),
    path('person/', views.Person.as_view(), name='person'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
