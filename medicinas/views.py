from django.shortcuts import render
from django.http import HttpResponse
from medicinas.models import NombreAnimal, Caracteristica, CitasAnimales ,Raza ,NombreDueño ,Historial
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.edit import UpdateView, CreateView, DeleteView




# Create your views here.

@login_required
def first_view(request):
    return render(request,'base.html')
@login_required
def animal(request):
	animal_list = NombreAnimal.objects.all()
	context = {'object_list': animal_list,'otra':'esta es la información'}
	return render(request, 'medicinas/animal.html', context)
@login_required
def animal_detail(request, animal_id):
	animal = NombreAnimal.objects.get(id=animal_id)
	context = {'object': animal}
	return render(request, 'medicinas/animal_detail.html', context)

#Caracteristicas	

@method_decorator(login_required, name='dispatch')
class CaracteristicaListView(ListView):
	model = Caracteristica

@method_decorator(login_required, name='dispatch')
class CaracteristicaDetailView(DetailView):
	model = Caracteristica

@method_decorator(login_required, name='dispatch')
class CaracteristicaUpdate(UpdateView):
	model = Caracteristica
	fields = '__all__'    
class CaracteristicaCreate(CreateView):
	model = Caracteristica
	fields = '__all__'
class CaracteristicaDelete(DeleteView):
    model = Caracteristica
    success_url = reverse_lazy('caracteristica-list')


#nombres de los animales con sus caracteristicas
class NombreAnimalUpdate(UpdateView):
	model = NombreAnimal
	fields = '__all__'    
class NombreAnimalCreate(CreateView):
	model = NombreAnimal
	fields = '__all__'
class NombreAnimalDelete(DeleteView):
    model = NombreAnimal
    success_url = reverse_lazy('animal-list')
class NombreAnimalListView(ListView):
	model = NombreAnimal

class NombreAnimalDetailView(DetailView):
	model = NombreAnimal		




#citas de animales
class CitasAnimalesUpdate(UpdateView):
	model = CitasAnimales
	fields = '__all__'    
class CitasAnimalesCreate(CreateView):
	model = CitasAnimales
	fields = '__all__'
class CitasAnimalesDelete(DeleteView):
    model = CitasAnimales
    success_url = reverse_lazy('citas-list')
class CitasAnimalesListView(ListView):
	model = CitasAnimales

class CitasAnimalesDetailView(DetailView):
	model = CitasAnimales	
#Raza	
class RazaUpdate(UpdateView):
	model = Raza
	fields = '__all__'    
class RazaCreate(CreateView):
	model = Raza
	fields = '__all__'
class RazaDelete(DeleteView):
    model = Raza
    success_url = reverse_lazy('raza-list')
class RazaListView(ListView):
	model = Raza
class RazaDetailView(DetailView):
	model = Raza
	
#nombre Dueño	
class NombreDueñoUpdate(UpdateView):
	model = NombreDueño
	fields = '__all__'    
class NombreDueñoCreate(CreateView):
	model = NombreDueño
	fields = '__all__'
class NombreDueñoDelete(DeleteView):
    model = NombreDueño
    success_url = reverse_lazy('nombredueno-list')
class NombreDueñoListView(ListView):
	model = NombreDueño
class NombreDueñoDetailView(DetailView):
	model = NombreDueño

#historial	
class HistorialUpdate(UpdateView):
	model = Historial
	fields = '__all__'    
class HistorialCreate(CreateView):
	model = Historial
	fields = '__all__'
class HistorialDelete(DeleteView):
    model = Historial
    success_url = reverse_lazy('historial-list')
class HistorialListView(ListView):
	model = Historial
class HistorialDetailView(DetailView):
	model = Historial    


