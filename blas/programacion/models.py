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
        return self.descripcion;


class ResultadoAprendizaje(models.Model):
    '''Resultados de Aprendizaje en terminología FP'''
    orden = models.CharField(max_length=2)
    materia = models.ForeignKey(Materia)
    pesoEnMateria = models.FloatField()
    descripcion = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.descripcion;


class Contenido(models.Model):
    '''Contenidos impartidos relacionados con cada resultado de aprendizaje '''
    resultadoAprendizaje = models.ForeignKey(models.ResultadoAprendizaje)
    descripcion = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.descripcion;


class CriterioEvaluacion(models.Model):
    resultadoAprendizaje = models.ForeignKey(models.ResultadoAprendizaje)
    descripcion = models.CharField(max_length=1000)
    indicador = models.ForeignKey(models.Indicador)

    def __unicode__(self):
        return self.descripcion;


class IndicadorResultadoAprendizaje(models.model):
    criterio = models.ForeignKey(models.CriterioEvaluacion)
    indicador = models.Foreignkey(models.Indicador)
    '''Peso del indicador para evaluar tal indicador '''
    pesoEnResultadoAprendizaje = models.FloatField()
    '''Valor mínimo'''
    minimo = models.IntegerField()
 

class Indicador(models.Model):
    ''' Indicador genérico  '''
    criterios = models.ManyToManyField(CriterioEvaluacion, through='IndicadorResultadoAprendizaje')
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.nombre;