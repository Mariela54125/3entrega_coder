from django.urls import path
from . import views

urlpatterns = [
    path ("", views.inicio, name="home"), 
    path ("ver_cursos", views.ver_cursos, name= "cursos"),
    path("profesores", views.profesores , name="profesores"),
    path("alta_curso/<nombre>", views.alta_curso),
    path ("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("alta_alumno", views.alumno_formulario),
    path('alta_alumno/', views.alta_alumno, name='alta_alumno'),
    path('buscar_alumno/', views.buscar_alumno, name='buscar_alumno'),
    path('buscar_a/', views.buscar_a, name='buscar_a'),
    path('buscar_alumno_resultado/', views.buscar_a, name='buscar_alumno_resultado'),
    path('ver_alumnos/', views.ver_alumnos, name='ver_alumnos'),
    path("ver_cursos", views.ver_cursos, name= "cursos"),
    path("alta_profesor", views.profesor_formulario),
    path('alta_profesor/', views.alta_profesor, name='alta_profesor'),
    path('buscar_profesor/', views.buscar_profesor, name='buscar_profesor'),
    path('buscar_p/', views.buscar_p, name='buscar_p'),
    path('buscar_profesor_resultado/', views.buscar_p, name='buscar_profesor_resultado'),
    path('ver_profesores/buscar_profesor/', views.buscar_profesor, name='buscar_profesor_ver_profesores'),
    path("elimina_alumno/<int:id>" , views.elimina_alumno , name="elimina_alumno"),
    path('elimina_profesor/<int:id>/', views.elimina_profesor, name='elimina_profesor'),
    path("editar_alumno/<int:id>", views.editar2 , name="editar_alumno"),
    path('editar_profesor/<int:id>/', views.editar3, name='editar_profesor'),
    path('ver_profesores/', views.ver_profesores, name='profesores'),
    path('ver_profesores/alta_profesor/', views.alta_profesor, name='alta_profesor_ver_profesores')
    
    

]
   

    
 
    

