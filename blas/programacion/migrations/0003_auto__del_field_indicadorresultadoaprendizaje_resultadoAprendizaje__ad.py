# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'IndicadorResultadoAprendizaje.resultadoAprendizaje'
        db.delete_column(u'programacion_indicadorresultadoaprendizaje', 'resultadoAprendizaje_id')

        # Adding field 'IndicadorResultadoAprendizaje.criterioEvaluacion'
        db.add_column(u'programacion_indicadorresultadoaprendizaje', 'criterioEvaluacion',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['normativa.CriterioEvaluacion']),
                      keep_default=False)

        # Deleting field 'PesoRAEnMateria.materia'
        db.delete_column(u'programacion_pesoraenmateria', 'materia_id')

        # Adding field 'PesoRAEnMateria.programacion'
        db.add_column(u'programacion_pesoraenmateria', 'programacion',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['programacion.Programacion']),
                      keep_default=False)

        # Adding field 'UnidadTrabajo.horasEstimadas'
        db.add_column(u'programacion_unidadtrabajo', 'horasEstimadas',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'IndicadorResultadoAprendizaje.resultadoAprendizaje'
        db.add_column(u'programacion_indicadorresultadoaprendizaje', 'resultadoAprendizaje',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['normativa.ResultadoAprendizaje']),
                      keep_default=False)

        # Deleting field 'IndicadorResultadoAprendizaje.criterioEvaluacion'
        db.delete_column(u'programacion_indicadorresultadoaprendizaje', 'criterioEvaluacion_id')

        # Adding field 'PesoRAEnMateria.materia'
        db.add_column(u'programacion_pesoraenmateria', 'materia',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['normativa.Materia']),
                      keep_default=False)

        # Deleting field 'PesoRAEnMateria.programacion'
        db.delete_column(u'programacion_pesoraenmateria', 'programacion_id')

        # Deleting field 'UnidadTrabajo.horasEstimadas'
        db.delete_column(u'programacion_unidadtrabajo', 'horasEstimadas')


    models = {
        u'normativa.competencia': {
            'Meta': {'ordering': "['orden']", 'object_name': 'Competencia'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'normativa.criterioevaluacion': {
            'Meta': {'ordering': "['resultadoAprendizaje', 'orden']", 'object_name': 'CriterioEvaluacion'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'resultadoAprendizaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.ResultadoAprendizaje']"})
        },
        u'normativa.materia': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Materia'},
            'competencias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['normativa.Competencia']", 'symmetrical': 'False'}),
            'horasSemanales': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'objetivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['normativa.Objetivo']", 'symmetrical': 'False'})
        },
        u'normativa.objetivo': {
            'Meta': {'ordering': "['orden']", 'object_name': 'Objetivo'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'normativa.resultadoaprendizaje': {
            'Meta': {'ordering': "['materia', 'orden']", 'object_name': 'ResultadoAprendizaje'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.Materia']"}),
            'orden': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'programacion.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'programacion.indicador': {
            'Meta': {'object_name': 'Indicador'},
            'criteriosEvaluacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['normativa.CriterioEvaluacion']", 'through': u"orm['programacion.IndicadorResultadoAprendizaje']", 'symmetrical': 'False'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'programacion.indicadorresultadoaprendizaje': {
            'Meta': {'object_name': 'IndicadorResultadoAprendizaje'},
            'criterioEvaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.CriterioEvaluacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programacion.Indicador']"}),
            'minimo': ('django.db.models.fields.IntegerField', [], {}),
            'pesoEnResultadoAprendizaje': ('django.db.models.fields.FloatField', [], {})
        },
        u'programacion.pesoraenmateria': {
            'Meta': {'ordering': "['programacion', 'resultadoAprendizaje']", 'object_name': 'PesoRAEnMateria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peso': ('django.db.models.fields.FloatField', [], {}),
            'programacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programacion.Programacion']"}),
            'resultadoAprendizaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.ResultadoAprendizaje']"})
        },
        u'programacion.programacion': {
            'Meta': {'ordering': "['materia']", 'object_name': 'Programacion'},
            'grupo': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['programacion.Grupo']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.Materia']"})
        },
        u'programacion.unidadtrabajo': {
            'Meta': {'object_name': 'UnidadTrabajo'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'horasEstimadas': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['programacion']