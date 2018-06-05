from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.views.generic import ListView
from django import forms



# Create your models here.
class NombreAnimal(models.Model):
    """ Nombres de las mascotas que llegan a la clinica """
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('animal-list')    
    
   

class Caracteristica(models.Model):
    """ Caracteristicas del animal """

    tipoAnimal = models.ForeignKey('NombreAnimal', on_delete=models.PROTECT )
    raza = models.ForeignKey('Raza', on_delete=models.PROTECT )
    nombreMascota = models.CharField(max_length=50)
    edad_años=models.IntegerField()
    color=models.CharField(max_length=50)
    Dueño = models.ForeignKey('NombreDueño', on_delete=models.PROTECT )
    photo = models.ImageField(upload_to='photos/')
    pub_date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombreMascota
      

    def get_absolute_url(self):
        return reverse('caracteristica-list')

@receiver(post_delete, sender=Caracteristica)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)
class Raza(models.Model):
    raza = models.CharField(max_length=50)
    def __str__(self):
        return self.raza
    def get_absolute_url(self):
        return reverse('raza-list')
   #clase del nombre del dueño     
class NombreDueño(models.Model):
    Dueño=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    def __str__(self):
        return self.Dueño
    def get_absolute_url(self):
        return reverse('nombredueno-list')    

class CitasAnimales(models.Model):
    """ agregar citas a los animales """
    nombreMascota = models.ForeignKey('Caracteristica', on_delete=models.PROTECT )
    tipodecita  = models.CharField(max_length=50)
    Dueño = models.ForeignKey('NombreDueño', on_delete=models.PROTECT )
    raza = models.ForeignKey('Raza', on_delete=models.PROTECT )
    motivo = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
       return self.Dueño
    def __str__(self):
        return self.nombreMascota
    
    def get_absolute_url(self):
        return reverse('citas-list')       

class Historial(models.Model):
    Dueño = models.ForeignKey('NombreDueño', on_delete=models.PROTECT )
    nombreMascota = models.ForeignKey('Caracteristica', on_delete=models.PROTECT )
    motivo=models.CharField(max_length=50)
    def __str__(self):
        return self.Dueño
    def get_absolute_url(self):
        return reverse('historial-list')

    

