# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Grupo'
        db.delete_table(u'normativa_grupo')

        # Deleting model 'Evaluacion'
        db.delete_table(u'normativa_evaluacion')


    def backwards(self, orm):
        # Adding model 'Grupo'
        db.create_table(u'normativa_grupo', (
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'normativa', ['Grupo'])

        # Adding model 'Evaluacion'
        db.create_table(u'normativa_evaluacion', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'normativa', ['Evaluacion'])


    models = {
        u'normativa.competencia': {
            'Meta': {'ordering': "['orden']", 'object_name': 'Competencia'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'normativa.contenido': {
            'Meta': {'ordering': "['materia', 'orden']", 'object_name': 'Contenido'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.Materia']"}),
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
        u'normativa.subcontenido': {
            'Meta': {'object_name': 'SubContenido'},
            'contenido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.Contenido']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['normativa']