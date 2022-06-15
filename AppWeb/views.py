from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, HttpResponse
from django.template import loader
from django import forms
from AppWeb.models import Curso, Profesor, Estudiantes, Entregable
from AppWeb.forms import CursoFormulario, ProfesorFormulario, EstudiantesFormulario, EntregablesFormulario


# Create your views here.

def inicio(request):
    return render(request, "AppWeb/inicio.html")
    

def curso(request):
    return render(request, "AppWeb/curso.html")

    
def profesores(request):
    return render(request, "AppWeb/profesores.html")

def estudiantes(request):
    return render(request, "AppWeb/estudiantes.html")

def entregables(request):
    return render(request, "AppWeb/entregables.html")    

def curso(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre= informacion['curso']
            camada= informacion['camada']
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()
        return render(request, "AppWeb/inicio.html")
    else:
        miFormulario = CursoFormulario()        
        
    return render(request, "AppWeb/curso.html", {"miFormulario":miFormulario})    

def profesores(request):
  if request.method == 'POST':
    miFormulario = ProfesorFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    nombre = informacion['nombre']
    apellido = informacion['apellido']
    email = informacion['email']
    profesion = informacion['profesion']

    profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
    profesor.save()
    return render(request, "AppWeb/inicio.html")
  else:
    miFormulario = ProfesorFormulario()
  return render(request, 'appWeb/profesores.html', {'miFormulario':miFormulario})

def estudiantes(request):
  if request.method == 'POST':
    miFormulario = EstudiantesFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    nombre = informacion['nombre']
    apellido = informacion['apellido']
    email = informacion['email']
    

    estudiantes = Estudiantes(nombre=nombre, apellido=apellido, email=email)
    estudiantes.save()
    return render(request, "AppWeb/inicio.html")
  else:
    miFormulario = EstudiantesFormulario()
  return render(request, 'appWeb/estudiantes.html', {'miFormulario':miFormulario})  

def entregables(request):
  if request.method == 'POST':
    miFormulario = EntregablesFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    nombre = informacion['nombre']
    fechaDeEntrega= informacion['fechaDeEntrega']
    entregado = informacion['entregado']
 

    entregables = Entregable(nombre=nombre, fechaDeEntrega=fechaDeEntrega, entregado=entregado)
    entregables.save()
    return render(request, "AppWeb/inicio.html")
  else:
    miFormulario = EntregablesFormulario()
  return render(request, 'appWeb/entregables.html', {'miFormulario':miFormulario})  

def buscar(request):

  if  request.GET["camada"]:

	  #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
    camada = request.GET['camada'] 
    cursos = Curso.objects.filter(camada__icontains=camada)

    return render(request, "AppWeb/inicio.html", {"cursos":cursos, "camada":camada})

  else: 

	  respuesta = "No enviaste datos"

    #No olvidar from django.http import HttpResponse
  return HttpResponse(respuesta)