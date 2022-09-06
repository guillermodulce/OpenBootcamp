from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Directores/index.html")

def guille(request):
    return HttpResponse("Hola, Guillermo!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
