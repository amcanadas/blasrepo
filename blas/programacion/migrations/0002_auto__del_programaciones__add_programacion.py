# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Programaciones'
        db.delete_table(u'programacion_programaciones')

        # Adding model 'Programacion'
        db.create_table(u'programacion_programacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.Materia'])),
        ))
        db.send_create_signal(u'programacion', ['Programacion'])

        # Adding M2M table for field grupo on 'Programacion'
        m2m_table_name = db.shorten_name(u'programacion_programacion_grupo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('programacion', models.ForeignKey(orm[u'programacion.programacion'], null=False)),
            ('grupo', models.ForeignKey(orm[u'programacion.grupo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['programacion_id', 'grupo_id'])


    def backwards(self, orm):
        # Adding model 'Programaciones'
        db.create_table(u'programacion_programaciones', (
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programacion.Grupo'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.Materia'])),
        ))
        db.send_create_signal(u'programacion', ['Programaciones'])

        # Deleting model 'Programacion'
        db.delete_table(u'programacion_programacion')

        # Removing M2M table for field grupo on 'Programacion'
        db.delete_table(db.shorten_name(u'programacion_programacion_grupo'))


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
        u'programacion.programacion': {
            'Meta': {'ordering': "['materia']", 'object_name': 'Programacion'},
            'grupo': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['programacion.Grupo']", 'symmetrical': 'False'}),
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