from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Movie(models.Model):
#   name = models.CharField(max_length=50)
#   image = models.ImageField(upload_to='files/covers')

class Casas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="casaspropias", null=True)
    casa_nombre= models.CharField(max_length=200)
    casa_descripcion = models.TextField(max_length=500)
    casa_direccion = models.CharField(max_length=200)
    casa_habitantes = models.IntegerField()
    casa_cuartos = models.IntegerField()
    casa_amueblada = models.BooleanField()
    casa_contacto = models.IntegerField()
    home_photo = models.ImageField(upload_to='files/covers', default='files/covers/missing.png')
    home_photo2 = models.ImageField(upload_to='files/covers', default='files/covers/missing.png')
    home_photo3 = models.ImageField(upload_to='files/covers', default='files/covers/missing.png')
    home_photo4 = models.ImageField(upload_to='files/covers', default='files/covers/missing.png')
    casa_aprobada = models.BooleanField(default=False)
    casa_rentada = models.BooleanField(default=False)
    casa_responsable = models.CharField(max_length=200)

    def __str__(self):
        return self.casa_nombre

class Blogs(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(max_length=1000)
    resumen = models.TextField(max_length=100)
    imagen = models.URLField()

    def __str__(self):
        return self.titulo
