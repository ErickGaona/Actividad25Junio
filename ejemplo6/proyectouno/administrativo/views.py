from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import Matricula, Estudiante
from administrativo.forms import MatriculaForm, MatriculaEditForm

# vista que permita presesentar las matriculas
# el nombre de la vista es index.

def index(request):
    matriculas = Matricula.objects.all()
    estudiantes = Estudiante.objects.all()

    # Agregar el total a cada estudiante
    for est in estudiantes:
        total = 0
        for m in est.lasmatriculas.all():
            for c in m.loscostos.all():
                total += c.costo
        est.total_general = total

    contexto = {
        'matriculas': matriculas,
        'estudiantes': estudiantes,
        'numero_matriculas': len(matriculas),
        'mititulo': "Listado de Matriculas y Estudiantes",
    }
    return render(request, 'index.html', contexto)



def detalle_matricula(request, id):
    """

    """

    matricula = Matricula.objects.get(pk=id)
    informacion_template = {'matricula': matricula}
    return render(request, 'detalle_matricula.html', informacion_template)


def crear_matricula(request):
    """
    """
    if request.method=='POST':
        formulario = MatriculaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = MatriculaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_matricula.html', diccionario)

def editar_matricula(request, id):
    """
    """
    matricula = Matricula.objects.get(pk=id)
    print("----------matricula")
    print(matricula)
    print("----------matricula")
    if request.method=='POST':
        formulario = MatriculaEditForm(request.POST, instance=matricula)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = MatriculaEditForm(instance=matricula)
    diccionario = {'formulario': formulario}

    return render(request, 'crear_matricula.html', diccionario)

def detalle_estudiante(request, id):
    """

    """

    estudiante = Estudiante.objects.get(pk=id)
    informacion_template = {'e': estudiante}
    return render(request, 'detalle_estudiante.html', informacion_template)


def costos_matricula(request, id):
    """
    """
    matricula = Matricula.objects.get(pk=id)
    costos = matricula.loscostos.all()
    informacion_template = {'matricula': matricula, 'costos': costos}
    return render(request, 'costos_matricula.html', informacion_template)


def listado_estudiantes_con_matriculas(request):
    estudiantes = Estudiante.objects.all()

    for est in estudiantes:
        total = 0
        for m in est.lasmatriculas.all():
            for c in m.loscostos.all():
                total += c.costo
        est.total_general = total  # este atributo lo usas en el template

    return render(request, 'index.html', {'estudiantes': estudiantes})


