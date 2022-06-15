from django.urls import path
from AppWeb import views



urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('curso/', views.curso, name='Curso'),
    path('profesores/', views.profesores, name='Profesores'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('entregables/', views.entregables, name='Entregables'),
    #path('cursoFormulario/', views.cursoFormulario, name='cursoFormulario'),
    #path('profesorFormulario/', profesorFormulario, name='profesorFormulario'),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
] 







