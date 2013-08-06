# -*- coding: utf-8 -*-
from django.db import models




class Competencia(models.Model):
    '''Competencias profesionales , Objetivos de Ciclo '''
    orden = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=1000)


class Objetivo(models.Model):
    ''' Cada uno de los objetivos generales del Ciclo '''
    orden = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=1000)


class Materia(models.Model):
    ''' Módulos '''
    nombre = models.CharField(max_length=100)
    ''' Competencias profesionales desarrolladas en la materia '''
    competencias = models.ManyToManyField(Competencia)
    ''' Objetivos del ciclo tratados en esta materia '''
    objetivos = models.ManyToManyField(Objetivo)

    def __unicode__(self):
        return self.nombre


class ResultadoAprendizaje(models.Model):
    '''Resultados de Aprendizaje en terminologia FP'''
    orden = models.CharField(max_length=2)
    materia = models.ForeignKey(Materia)
    pesoEnMateria = models.FloatField()
    descripcion = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.descripcion


class Contenido(models.Model):
    '''Contenidos impartidos relacionados con cada resultado de aprendizaje '''
    resultadoAprendizaje = models.ForeignKey(ResultadoAprendizaje)
    descripcion = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.descripcion


class Indicador(models.Model):
    ''' Indicador genérico  '''
    resultadoAprendizaje = models.ManyToManyField(ResultadoAprendizaje, through='IndicadorResultadoAprendizaje')
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.nombre


class CriterioEvaluacion(models.Model):
    resultadoAprendizaje = models.ForeignKey(ResultadoAprendizaje)
    descripcion = models.CharField(max_length=1000)
    indicador = models.ForeignKey(Indicador)

    def __unicode__(self):
        return self.descripcion


class IndicadorResultadoAprendizaje(models.Model):
    resultadoAprendizaje = models.ForeignKey(ResultadoAprendizaje)
    indicador = models.ForeignKey(Indicador)
    '''Peso del indicador para evaluar tal indicador '''
    pesoEnResultadoAprendizaje = models.FloatField()
    '''Valor mínimo'''
    minimo = models.IntegerField()