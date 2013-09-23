from django.contrib import admin
from normativa.models import *


class CriterioEvaluacionInline(admin.TabularInline):
	model = CriterioEvaluacion
	extra = 8

class SubContenidoInline(admin.TabularInline):
	model = SubContenido
	extra = 8

class ResultadoAprendizajeInline(admin.TabularInline):
	model = ResultadoAprendizaje
	extra = 8

class ContenidoInline(admin.TabularInline):
	model = Contenido
	extra = 8

class CriterioEvaluacionInline(admin.TabularInline):
	model = CriterioEvaluacion
	extra = 8

class ResultadoAprendizajeAdmin(admin.ModelAdmin):
    list_display = ('orden', 'descripcion', 'materia')
    list_display_links = ('orden', 'descripcion')
    inlines = [CriterioEvaluacionInline]

class ContenidoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','materia')
    inlines = [SubContenidoInline] 

class MateriaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	inlines = [ResultadoAprendizajeInline,ContenidoInline]

class CriterioEvaluacionAdmin(admin.ModelAdmin):
	list_display = ('descripcion','orden','resultadoAprendizaje','materia')
	list_display_links = ('descripcion', 'orden')
	list_filter = ('resultadoAprendizaje',)
	inlines = [ResultadoAprendizajeInline,ContenidoInline]

admin.site.register(Materia,MateriaAdmin)
admin.site.register(Competencia)
admin.site.register(Objetivo)
admin.site.register(ResultadoAprendizaje,ResultadoAprendizajeAdmin)
admin.site.register(CriterioEvaluacion,CriterioEvaluacionAdmin)
admin.site.register(Contenido,ContenidoAdmin)
#admin.site.register(SubContenido)
#admin.site.register(Evaluacion)