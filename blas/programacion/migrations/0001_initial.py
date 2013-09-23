# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grupo'
        db.create_table(u'programacion_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'programacion', ['Grupo'])

        # Adding model 'Programaciones'
        db.create_table(u'programacion_programaciones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.Materia'])),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programacion.Grupo'])),
        ))
        db.send_create_signal(u'programacion', ['Programaciones'])

        # Adding model 'PesoRAEnMateria'
        db.create_table(u'programacion_pesoraenmateria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.Materia'])),
            ('resultadoAprendizaje', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.ResultadoAprendizaje'])),
            ('peso', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'programacion', ['PesoRAEnMateria'])

        # Adding model 'UnidadTrabajo'
        db.create_table(u'programacion_unidadtrabajo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'programacion', ['UnidadTrabajo'])

        # Adding model 'Indicador'
        db.create_table(u'programacion_indicador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'programacion', ['Indicador'])

        # Adding model 'IndicadorResultadoAprendizaje'
        db.create_table(u'programacion_indicadorresultadoaprendizaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resultadoAprendizaje', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.ResultadoAprendizaje'])),
            ('indicador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programacion.Indicador'])),
            ('pesoEnResultadoAprendizaje', self.gf('django.db.models.fields.FloatField')()),
            ('minimo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'programacion', ['IndicadorResultadoAprendizaje'])


    def backwards(self, orm):
        # Deleting model 'Grupo'
        db.delete_table(u'programacion_grupo')

        # Deleting model 'Programaciones'
        db.delete_table(u'programacion_programaciones')

        # Deleting model 'PesoRAEnMateria'
        db.delete_table(u'programacion_pesoraenmateria')

        # Deleting model 'UnidadTrabajo'
        db.delete_table(u'programacion_unidadtrabajo')

        # Deleting model 'Indicador'
        db.delete_table(u'programacion_indicador')

        # Deleting model 'IndicadorResultadoAprendizaje'
        db.delete_table(u'programacion_indicadorresultadoaprendizaje')


    models = {
        u'normativa.competencia': {
            'Meta': {'ordering': "['orden']", 'object_name': 'Competencia'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.CharField', [], {'max_length': '2'})
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
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resultadoAprendizaje': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['normativa.ResultadoAprendizaje']", 'through': u"orm['programacion.IndicadorResultadoAprendizaje']", 'symmetrical': 'False'})
        },
        u'programacion.indicadorresultadoaprendizaje': {
            'Meta': {'object_name': 'IndicadorResultadoAprendizaje'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programacion.Indicador']"}),
            'minimo': ('django.db.models.fields.IntegerField', [], {}),
            'pesoEnResultadoAprendizaje': ('django.db.models.fields.FloatField', [], {}),
            'resultadoAprendizaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.ResultadoAprendizaje']"})
        },
        u'programacion.pesoraenmateria': {
            'Meta': {'ordering': "['materia', 'resultadoAprendizaje']", 'object_name': 'PesoRAEnMateria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.Materia']"}),
            'peso': ('django.db.models.fields.FloatField', [], {}),
            'resultadoAprendizaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.ResultadoAprendizaje']"})
        },
        u'programacion.programaciones': {
            'Meta': {'object_name': 'Programaciones'},
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programacion.Grupo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.Materia']"})
        },
        u'programacion.unidadtrabajo': {
            'Meta': {'object_name': 'UnidadTrabajo'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['programacion']