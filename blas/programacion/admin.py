from django.contrib import admin
from programacion.models import *

class ProgramacionAdmin(admin.ModelAdmin):
    list_display = ('materia','grupos')

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre')

class PesoRAEnMateriaAdmin(admin.ModelAdmin):

    list_display = ('resultadoAprendizaje','peso','programacion')
    list_display_links = ('resultadoAprendizaje', 'peso')
    list_filter = ('programacion',)

    ''' def lookup_allowed(self, key, *args, **kwargs):
        return True'''

    def lookup_allowed(self, lookup, value):
        return True

class IndicadorCriterioEvaluacionInline(admin.TabularInline):
    model = IndicadorCriterioEvaluacion
    extra = 8

class IndicadorAdmin(admin.ModelAdmin):

    list_display = ('nombre','descripcion','minimoValor')
    list_display_links = ('nombre', 'descripcion')
    inlines = [IndicadorCriterioEvaluacionInline] 


admin.site.register(Grupo,GrupoAdmin)
admin.site.register(Programacion,ProgramacionAdmin)
admin.site.register(PesoRAEnMateria,PesoRAEnMateriaAdmin)
admin.site.register(Indicador,IndicadorAdmin)
admin.site.register(UnidadTrabajo)
#admin.site.register(ResultadoAprendizaje)
