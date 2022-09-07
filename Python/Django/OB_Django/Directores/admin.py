from django.contrib import admin

# Register your models here.
from .models import Directores, Actores, Peliculas

admin.site.register(Directores)
admin.site.register(Actores)
admin.site.register(Peliculas)
