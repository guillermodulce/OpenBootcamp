from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre del director")
    country = models.CharField(max_length=64, null=True, help_text="Pais de origen del director")
    born_date = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.name

class Actor(models.Model):
    actor_name = models.CharField(max_length=64, help_text="Nombre del actor o actriz")

    def __str__(self):
        return self.actor_name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=4, null=True)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Descripción de la pelicula')
    performer = models.ManyToManyField(Actor)

def __str__(self):
    return self.title




