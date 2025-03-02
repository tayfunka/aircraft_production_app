from django.urls import path
from . import views

app_name = 'aircraft'

urlpatterns = [
    path('api/aircraft-type-create/', views.CreateAircraftType.as_view(),
         name='aircraft-type-create-api'),
    path('api/aircraft-type-list/', views.ListAircraftType.as_view(),
         name='aircraft-type-list-api'),
    path('api/assemble-aircraft/', views.AssembleAircraft.as_view(),
         name='assemble-aircraft-api'),
    path('api/aircraft-list-api/', views.ListAircraftAssembly.as_view(),
         name='aircraft-list-api'),
    path('assemble-aircraft/', views.AssembleAircraftView.as_view(),
         name='assemble-aircraft'),
    path('aircraft-list/', views.ListAircraftAssemblyView.as_view(),
         name='aircraft-list'),
    path('api/aircraft-list-datatable/', views.AircraftAssemblyListViewDatatable.as_view(),
         name='aircraft-list-datatable'),
]
