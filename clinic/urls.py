from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('owners/', views.owner_list, name='owner_list'),
    path('owners/new/', views.owner_create, name='owner_create'),
    path('owners/<int:pk>/', views.owner_detail, name='owner_detail'),
    path('owners/<int:pk>/edit/', views.owner_edit, name='owner_edit'),
    path('owners/<int:owner_pk>/pets/new/', views.pet_create, name='pet_create'),
    path('pets/<int:pet_pk>/visits/new/', views.visit_create, name='visit_create'),
    path('vets/', views.vet_list, name='vet_list'),
]
