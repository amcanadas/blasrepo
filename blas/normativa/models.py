# -*- coding: utf-8 -*-
import re
from django.db import models


class Competencia(models.Model):
    '''Competencias profesionales , Objetivos de Ciclo '''
    orden = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.orden+'. '+self.descripcion

    class Meta:
        ordering = ['orden']
        verbose_name_plural = 'Competencias profesionales'
        verbose_name = 'Competencia profesional'


class Objetivo(models.Model):
    ''' Cada uno de los objetivos generales del Ciclo '''
    orden = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.orden+'. '+self.descripcion

    class Meta:
        ordering = ['orden']
        verbose_name_plural = 'Objetivos Generales del ciclo'
        verbose_name = 'Objetivo general'


class Materia(models.Model):
    ''' Módulos '''
    nombre = models.CharField(max_length=100)
    ''' Competencias profesionales desarrolladas en la materia '''
    competencias = models.ManyToManyField(Competencia)
    ''' Objetivos del ciclo tratados en esta materia '''
    objetivos = models.ManyToManyField(Objetivo)
    horasSemanales = models.IntegerField()

    def nombrecorto(self):
    	return re.sub('[^A-Z]', '', self.nombre)

    def __unicode__(self):
        return self.nombre

    class Meta:
    	ordering = ['nombre']
        verbose_name_plural = 'Modulos'
        verbose_name = 'Modulo'


class ResultadoAprendizaje(models.Model):
    '''Resultados de Aprendizaje en terminologia FP'''
    orden = models.CharField(max_length=2)
    materia = models.ForeignKey(Materia)
    descripcion = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return (self.materia.nombrecorto()+'.'+self.orden+'.'+self.descripcion)[:80]

    class Meta:
        ordering = ['materia','orden']
        verbose_name_plural = 'Resultados de Aprendizaje'
        verbose_name = 'Resultado de Aprendizaje'


class CriterioEvaluacion(models.Model):
    resultadoAprendizaje = models.ForeignKey(ResultadoAprendizaje)
    orden = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=1000)

    def materia(self):
        return self.resultadoAprendizaje.materia

    def __unicode__(self):
        return self.materia()+'.'+self.resultadoAprendizaje.orden+'.'+self.orden+'.'+self.descripcion[:30]

    class Meta:
        ordering = ['resultadoAprendizaje','orden']
        verbose_name_plural = 'Criterios de Evaluación'
        verbose_name = 'Criterio de Evaluación'

class Contenido(models.Model):
    '''Contenidos impartidos relacionados con cada resultado de aprendizaje '''
    materia = models.ForeignKey(Materia)
    orden = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.orden+'. '+self.descripcion

    class Meta:
        ordering = ['materia','orden']
        verbose_name_plural = 'Contenidos'
        verbose_name = 'Contenido'


class SubContenido(models.Model):
    '''Cada uno de los contenidos '''
    contenido = models.ForeignKey(Contenido)
    orden = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.descripcion
