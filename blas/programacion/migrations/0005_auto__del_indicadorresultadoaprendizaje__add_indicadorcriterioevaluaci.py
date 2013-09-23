# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'IndicadorResultadoAprendizaje'
        db.delete_table(u'programacion_indicadorresultadoaprendizaje')

        # Adding model 'IndicadorCriterioEvaluacion'
        db.create_table(u'programacion_indicadorcriterioevaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('criterioEvaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.CriterioEvaluacion'])),
            ('indicador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programacion.Indicador'])),
            ('peso', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'programacion', ['IndicadorCriterioEvaluacion'])

        # Adding field 'Indicador.minimoValor'
        db.add_column(u'programacion_indicador', 'minimoValor',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Indicador.escalaValor'
        db.add_column(u'programacion_indicador', 'escalaValor',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'UnidadTrabajo.horasEstimadas'
        db.delete_column(u'programacion_unidadtrabajo', 'horasEstimadas')

        # Adding field 'UnidadTrabajo.descripcion'
        db.add_column(u'programacion_unidadtrabajo', 'descripcion',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True),
                      keep_default=False)

        # Adding field 'UnidadTrabajo.horas'
        db.add_column(u'programacion_unidadtrabajo', 'horas',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2),
                      keep_default=False)

        # Adding field 'UnidadTrabajo.orden'
        db.add_column(u'programacion_unidadtrabajo', 'orden',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'IndicadorResultadoAprendizaje'
        db.create_table(u'programacion_indicadorresultadoaprendizaje', (
            ('minimo', self.gf('django.db.models.fields.IntegerField')()),
            ('indicador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programacion.Indicador'])),
            ('pesoEnResultadoAprendizaje', self.gf('django.db.models.fields.FloatField')()),
            ('criterioEvaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.CriterioEvaluacion'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'programacion', ['IndicadorResultadoAprendizaje'])

        # Deleting model 'IndicadorCriterioEvaluacion'
        db.delete_table(u'programacion_indicadorcriterioevaluacion')

        # Deleting field 'Indicador.minimoValor'
        db.delete_column(u'programacion_indicador', 'minimoValor')

        # Deleting field 'Indicador.escalaValor'
        db.delete_column(u'programacion_indicador', 'escalaValor')

        # Adding field 'UnidadTrabajo.horasEstimadas'
        db.add_column(u'programacion_unidadtrabajo', 'horasEstimadas',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2),
                      keep_default=False)

        # Deleting field 'UnidadTrabajo.descripcion'
        db.delete_column(u'programacion_unidadtrabajo', 'descripcion')

        # Deleting field 'UnidadTrabajo.horas'
        db.delete_column(u'programacion_unidadtrabajo', 'horas')

        # Deleting field 'UnidadTrabajo.orden'
        db.delete_column(u'programacion_unidadtrabajo', 'orden')


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
            'criteriosEvaluacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['normativa.CriterioEvaluacion']", 'through': u"orm['programacion.IndicadorCriterioEvaluacion']", 'symmetrical': 'False'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'descripcionAlumnos': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'escalaValor': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimoValor': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'programacion.indicadorcriterioevaluacion': {
            'Meta': {'object_name': 'IndicadorCriterioEvaluacion'},
            'criterioEvaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['normativa.CriterioEvaluacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programacion.Indicador']"}),
            'peso': ('django.db.models.fields.FloatField', [], {'null': 'True'})
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
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'evaluacion': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '20'}),
            'horas': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicadores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['programacion.Indicador']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'subcontenidos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'subcontenidos'", 'symmetrical': 'False', 'to': u"orm['normativa.SubContenido']"})
        }
    }

    complete_apps = ['programacion']