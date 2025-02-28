from django.urls import path
from . import views

app_name = 'part'

urlpatterns = [
    path('api/part-create/', views.PartCreateView.as_view(),
         name='part-create-api'),
    path('api/part-list/', views.PartListView.as_view(),
         name='personnel-authenticate-api'),

    path('api/part-delete/', views.PartDeleteView.as_view(),
         name='part-delete-api'),

    path('part-create/', views.PartCreate.as_view(),
         name='part-create'),

    path('part-list/', views.PartList.as_view(), name='part-list'),
]
