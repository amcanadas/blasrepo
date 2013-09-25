# -*- coding: utf-8 -*-
from django.db import models
from normativa import models as normas

class Grupo(models.Model):
    ''' Grupos de alumnos '''
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.codigo

class Evaluaciones(object):
    PRIMERA = '1'
    SEGUNDA = '2'
    FINAL = 'O'
    EXTRAORDINARIA = 'E'
    EVALUACIONES = (
        (PRIMERA, 'Primera'),
        (SEGUNDA, 'Segunda'),
        (FINAL, 'Ordinaria 1ª'),
        (EXTRAORDINARIA, 'Ordinaria 2ª'),
    )


class Programacion(models.Model):
    materia = models.ForeignKey(normas.Materia)
    grupo = models.ManyToManyField(Grupo)

    def __unicode__(self):
        return self.materia.nombre + ' (' + (self.grupos()) +')'

    def grupos(self):
        return ', '.join([ g.codigo for g in self.grupo.all() ])
    grupos.short_description = 'Grupos'
    grupos.allow_tags = True

    class Meta:
        ordering = ['materia']
        verbose_name_plural = 'Programaciones didácticas'
        verbose_name = 'Programación didáctica'

class PesoRAEnMateria(models.Model):
    ''' Pesos de cada resultado de aprendizaje en la materia '''
    programacion = models.ForeignKey(Programacion)
    resultadoAprendizaje = models.ForeignKey(normas.ResultadoAprendizaje)
    peso = models.FloatField()
    
    @property
    def pesoNormalizado(self):
        total=PesoRAEnMateria.objects.filter(programacion=self.programacion).aggregate(models.Sum('peso'))['peso__sum']
        return (self.peso/total)*100

    class Meta:
        ordering = ['programacion','resultadoAprendizaje']
        verbose_name_plural = 'Pesos de Resultados de Aprendizaje en Materia'
        verbose_name = 'Peso de Resultado de Aprendizaje en Materia'
        

class Indicador(models.Model):
    ''' Indicador genérico  '''
    criteriosEvaluacion = models.ManyToManyField(normas.CriterioEvaluacion, through='IndicadorCriterioEvaluacion')
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    descripcionAlumnos = models.CharField(max_length=1000)
    '''Valor mínimo'''
    minimoValor = models.IntegerField(null=True,blank=True)
    ''' Escala '''
    ''' TODO: poner escala a cualitativo/cuantitativo3/cuantitativo4'''
    escalaValor = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Indicadores'
        verbose_name = 'Indicador'


class IndicadorCriterioEvaluacion(models.Model):
    ''' Relación de indicador con criterios de evaluación '''
    criterioEvaluacion = models.ForeignKey(normas.CriterioEvaluacion)
    indicador = models.ForeignKey(Indicador)
    '''Peso del indicador para evaluar resultado de aprendizaje '''
    peso = models.FloatField(null=True,blank=True)

    class Meta:
        ordering = ['indicador']
        verbose_name_plural = 'Criterios de cada Indicador'
        verbose_name = 'Criterio de un indicador'
    

class UnidadTrabajo(models.Model):
    ''' Unidades de trabajo '''
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000, null=True,blank=True)
    ''' Horas dedicadas a la imágen '''
    horas = models.IntegerField(max_length=2)
    '''resultadoAprendizaje = models.ForeignKey(normas.ResultadoAprendizaje)'''
    ''' Contenidos o subcontenidos incluidos en la unidad de trabajo '''
    contenidos = models.ManyToManyField(normas.Contenido, related_name='contenidos')
    subcontenidos = models.ManyToManyField(normas.SubContenido, related_name='subcontenidos')
    ''' Indicadores utilizados en su evaluación '''
    ''' TODO: añadir un atributo a la relación, la importancia del indicador para la UT '''
    indicadores = models.ManyToManyField(Indicador)
    ''' Temporalización (evaluación en la que se impartirá) '''
    orden = models.IntegerField(max_length=2)
    evaluacion = models.CharField(max_length=20,choices=Evaluaciones.EVALUACIONES,
                                      default=Evaluaciones.PRIMERA)

    def __unicode__(self):
        return self.nombre