# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CriterioEvaluacion.orden'
        db.add_column(u'normativa_criterioevaluacion', 'orden',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CriterioEvaluacion.orden'
        db.delete_column(u'normativa_criterioevaluacion', 'orden')


    models = {
        u'normativa.competencia': {
            'Meta': {'ordering': "['orden']", 'object_name': 'Competencia'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'normativa.contenido': {
            'Meta': {'object_name': 'Contenido'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resultadoAprendizaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.ResultadoAprendizaje']"})
        },
        u'normativa.criterioevaluacion': {
            'Meta': {'ordering': "['resultadoAprendizaje', 'orden']", 'object_name': 'CriterioEvaluacion'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'resultadoAprendizaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.ResultadoAprendizaje']"})
        },
        u'normativa.evaluacion': {
            'Meta': {'object_name': 'Evaluacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'normativa.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        u'normativa.subcontenido': {
            'Meta': {'object_name': 'SubContenido'},
            'contenido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.Contenido']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['normativa']