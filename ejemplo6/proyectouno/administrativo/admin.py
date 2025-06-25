from django.contrib import admin
from administrativo.models import Estudiante, Modulo, Matricula, costosMatricula

# Importar las clases del modelo


# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class EstudianteAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante')
    search_fields = ('nombre', 'cedula')

# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin
admin.site.register(Estudiante, EstudianteAdmin)

admin.site.register(Modulo)

# admin.site.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('estudiante', 'modulo', 'comentario')
    search_fields = ('estudiante__nombre', 'modulo__nombre')

admin.site.register(Matricula, MatriculaAdmin)


class costosMatriculaAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('matricula', 'valor')
    search_fields = ('matricula__estudiante__nombre',)

admin.site.register(costosMatricula)  

