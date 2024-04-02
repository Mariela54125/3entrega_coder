from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.forms import Alumno_formulario
from AppCoder.forms import Profesor_formulario
from AppCoder.models import Alumno
from AppCoder.models import Profesores

# Create your views here.
#CURSO#
def inicio(request):
    return render(request, "padre.html")

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumnos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)
    

def profesores(request):
    return render(request , "profesores.html")

def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")

def buscar_curso(request):

    return render(request, "buscar_curso.html")


def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
def elimina_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})

def editar(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})

          
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})

#ALUMNO#

def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre=datos["nombre"], apellido=datos["apellido"], dni=datos["dni"])
            alumno.save()
            return render(request, "formulario2.html")
    return render(request, "formulario2.html")

def alta_alumno(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')

        alumno = Alumno(nombre=nombre, apellido=apellido, dni=dni)
        alumno.save()
        
        texto = f"Se guardó en la BD el alumno: {alumno.nombre} {alumno.apellido} con DNI: {alumno.dni}"
        return HttpResponse(texto)
    else:
        return HttpResponse("Se esperaba una solicitud POST para agregar un nuevo alumno")

def buscar_alumno(request):

    return render(request, "buscar_alumno.html")

def buscar_a(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda_alumno.html", {"alumnos": alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")



def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, "ver_alumnos.html", {"alumnos": alumnos})

def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})


def elimina_alumno(request , id ):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
            
    alumno = Alumno.objects.all()

    return render(request , "alumnos.html" , {"alumno":alumno})

def editar2(request , id):

    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.apellido = datos["apellido"]
            alumno.dni = datos["dni"]
            alumno.save()

            alumno = Alumno.objects.all()

            return render(request , "Alumnos.html" , {"alumnos":alumno})

          
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre , "apellido":alumno.apellido , "dni":alumno.dni})
    
    return render( request , "editar_alumno.html" , {"mi_formulario": mi_formulario , "alumno":alumno})



#PROFESORES#

def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Profesor = Profesores(nombre=datos["nombre"], apellido=datos["apellido"], dni=datos["dni"])
            Profesor.save()
            return render(request, "formulario3.html")
    return render(request, "formulario3.html")

def alta_profesor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')

        nuevo_Profesor = Profesores(nombre=nombre, apellido=apellido, dni=dni)
        nuevo_Profesor.save()
        
        texto = f"Se guardó en la BD el profesor: {nuevo_Profesor.nombre} {nuevo_Profesor.apellido} con DNI: {nuevo_Profesor.dni}"
        return HttpResponse(texto)
    else:
        return HttpResponse("Se esperaba una solicitud POST para agregar un nuevo profesor")

def buscar_profesor(request):

    return render(request, "buscar_profesor.html")

def buscar_p(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        profesor = Profesores.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda_profesor.html", {"profesor": profesor})
    else:
        return HttpResponse("Ingrese el nombre del profesor")

 

def ver_profesores(request):
    profesores = Profesores.objects.all()  
    return render(request, "profesores.html", {"profesores": profesores})  

def profesores(request):
    lista_profesor = Profesores.objects.all()
    return render(request, 'profesores.html', {'profesores': lista_profesor})


def elimina_profesor(request , id ):
    profesor = Profesores.objects.get(id=id)
    profesor.delete()
            
    profesores = Profesores.objects.all()

    return render(request , "profesores.html" , {"profesores":profesores})


def editar3(request , id):

    profesor = Profesores.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.apellido = datos["apellido"]
            profesor.dni = datos["dni"]
            profesor.save()

            profesor = Profesores.objects.all()

            return render(request , "profesores.html" , {"profesor":profesor})

          
    else:
        mi_formulario = Profesor_formulario(initial={"nombre":profesor.nombre , "apellido":profesor.apellido , "dni":profesor.dni})
    
    return render( request , "editar_profesor.html" , {"mi_formulario": mi_formulario , "profesor":profesor})
