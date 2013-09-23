# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Indicador.descripcionAlumnos'
        db.add_column(u'programacion_indicador', 'descripcionAlumnos',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=1000),
                      keep_default=False)

        # Adding field 'UnidadTrabajo.evaluacion'
        db.add_column(u'programacion_unidadtrabajo', 'evaluacion',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=20),
                      keep_default=False)

        # Adding M2M table for field contenidos on 'UnidadTrabajo'
        m2m_table_name = db.shorten_name(u'programacion_unidadtrabajo_contenidos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unidadtrabajo', models.ForeignKey(orm[u'programacion.unidadtrabajo'], null=False)),
            ('contenido', models.ForeignKey(orm[u'normativa.contenido'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unidadtrabajo_id', 'contenido_id'])

        # Adding M2M table for field subcontenidos on 'UnidadTrabajo'
        m2m_table_name = db.shorten_name(u'programacion_unidadtrabajo_subcontenidos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unidadtrabajo', models.ForeignKey(orm[u'programacion.unidadtrabajo'], null=False)),
            ('subcontenido', models.ForeignKey(orm[u'normativa.subcontenido'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unidadtrabajo_id', 'subcontenido_id'])

        # Adding M2M table for field indicadores on 'UnidadTrabajo'
        m2m_table_name = db.shorten_name(u'programacion_unidadtrabajo_indicadores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unidadtrabajo', models.ForeignKey(orm[u'programacion.unidadtrabajo'], null=False)),
            ('indicador', models.ForeignKey(orm[u'programacion.indicador'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unidadtrabajo_id', 'indicador_id'])


    def backwards(self, orm):
        # Deleting field 'Indicador.descripcionAlumnos'
        db.delete_column(u'programacion_indicador', 'descripcionAlumnos')

        # Deleting field 'UnidadTrabajo.evaluacion'
        db.delete_column(u'programacion_unidadtrabajo', 'evaluacion')

        # Removing M2M table for field contenidos on 'UnidadTrabajo'
        db.delete_table(db.shorten_name(u'programacion_unidadtrabajo_contenidos'))

        # Removing M2M table for field subcontenidos on 'UnidadTrabajo'
        db.delete_table(db.shorten_name(u'programacion_unidadtrabajo_subcontenidos'))

        # Removing M2M table for field indicadores on 'UnidadTrabajo'
        db.delete_table(db.shorten_name(u'programacion_unidadtrabajo_indicadores'))


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
            'descripcionAlumnos': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
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
            'contenidos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contenidos'", 'symmetrical': 'False', 'to': u"orm['normativa.Contenido']"}),
            'evaluacion': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '20'}),
            'horasEstimadas': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicadores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['programacion.Indicador']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subcontenidos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'subcontenidos'", 'symmetrical': 'False', 'to': u"orm['normativa.SubContenido']"})
        }
    }

    complete_apps = ['programacion']