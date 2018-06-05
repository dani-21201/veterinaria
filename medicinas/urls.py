
from django.contrib import admin
from django.urls import path ,include
from medicinas import views



urlpatterns = [
    path('',views.first_view,name='base'),
    path('animal/',views.animal,name='animal-list'),
    path('animal/<int:animal_id>/detail/', views.animal_detail, name='animal-detail'),
    path('caracteristica/', views.CaracteristicaListView.as_view(), name='caracteristica-list'),
    path('caracteristica/<int:pk>/detail/', views.CaracteristicaDetailView.as_view(), name='caracteristica-detail'),
    # Update caracteristica
    path('caracteristica/<int:pk>/update/', views.CaracteristicaUpdate.as_view(), name='caracteristica-update'),
    #Create caracteristica
    path('caracteristica/create/', views.CaracteristicaCreate.as_view(), name='caracteristica-create'),
    #Delete caracteristica
    path('caracteristica/<int:pk>/delete/', views.CaracteristicaDelete.as_view(), name='caracteristica-delete'),
     # Update animal
    path('animal/<int:pk>/update/', views.NombreAnimalUpdate.as_view(), name='animal-update'),
    #Create animal
    path('animal/create/', views.NombreAnimalCreate.as_view(), name='animal-create'),
    #Delete animal
    path('animal/<int:pk>/delete/', views.NombreAnimalDelete.as_view(), name='animal-delete'),


    #citas
    path('citas/', views.CitasAnimalesListView.as_view(), name='citas-list'),
    
    path('citas/<int:pk>/detail/', views.CitasAnimalesDetailView.as_view(), name='citas-detail'),
    # Update citas
    path('citas/<int:pk>/update/', views.CitasAnimalesUpdate.as_view(), name='citas-update'),
    #Create citas
    path('citas/create/', views.CitasAnimalesCreate.as_view(), name='citas-create'),
    #Delete citas
    path('citas/<int:pk>/delete/', views.CitasAnimalesDelete.as_view(), name='citas-delete'),

    #Raza
    
    path('raza/', views.RazaListView.as_view(), name='raza-list'),
    
    path('raza/<int:pk>/detail/', views.RazaDetailView.as_view(), name='raza-detail'),
    # Update raza
    path('raza/<int:pk>/update/', views.RazaUpdate.as_view(), name='raza-update'),
    #Create raza
    path('raza/create/', views.RazaCreate.as_view(), name='raza-create'),
    #Delete raza
    path('raza/<int:pk>/delete/', views.RazaDelete.as_view(), name='raza-delete'),


    #nombre dueño

  
    
    path('dueño/', views.NombreDueñoListView.as_view(), name='nombredueno-list'),
    
    path('dueño/<int:pk>/detail/', views.NombreDueñoDetailView.as_view(), name='nombredueno-detail'),
    # Update NombreDueño
    path('dueño/<int:pk>/update/', views.NombreDueñoUpdate.as_view(), name='nombredueno-update'),
    #Create NombreDueño
    path('dueño/create/', views.NombreDueñoCreate.as_view(), name='nombredueno-create'),
    #Delete NombreDueño
    path('dueño/<int:pk>/delete/', views.NombreDueñoDelete.as_view(), name='nombredueno-delete'),

    #historial

    path('historial/', views.HistorialListView.as_view(), name='historial-list'),
    
    path('historial/<int:pk>/detail/', views.HistorialDetailView.as_view(), name='historial-detail'),
    # Update historial
    path('historial/<int:pk>/update/', views.HistorialUpdate.as_view(), name='historial-update'),
    #Create historial
    path('historial/create/', views.HistorialCreate.as_view(), name='historial-create'),
    #Delete historial
    path('historial/<int:pk>/delete/', views.HistorialDelete.as_view(), name='historial-delete'),

]