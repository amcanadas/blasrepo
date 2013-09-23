# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Competencia'
        db.create_table(u'normativa_competencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orden', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'normativa', ['Competencia'])

        # Adding model 'Objetivo'
        db.create_table(u'normativa_objetivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orden', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'normativa', ['Objetivo'])

        # Adding model 'Materia'
        db.create_table(u'normativa_materia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('horasSemanales', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'normativa', ['Materia'])

        # Adding M2M table for field competencias on 'Materia'
        m2m_table_name = db.shorten_name(u'normativa_materia_competencias')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('materia', models.ForeignKey(orm[u'normativa.materia'], null=False)),
            ('competencia', models.ForeignKey(orm[u'normativa.competencia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['materia_id', 'competencia_id'])

        # Adding M2M table for field objetivos on 'Materia'
        m2m_table_name = db.shorten_name(u'normativa_materia_objetivos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('materia', models.ForeignKey(orm[u'normativa.materia'], null=False)),
            ('objetivo', models.ForeignKey(orm[u'normativa.objetivo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['materia_id', 'objetivo_id'])

        # Adding model 'ResultadoAprendizaje'
        db.create_table(u'normativa_resultadoaprendizaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orden', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.Materia'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'normativa', ['ResultadoAprendizaje'])

        # Adding model 'CriterioEvaluacion'
        db.create_table(u'normativa_criterioevaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resultadoAprendizaje', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.ResultadoAprendizaje'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'normativa', ['CriterioEvaluacion'])

        # Adding model 'Contenido'
        db.create_table(u'normativa_contenido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resultadoAprendizaje', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.ResultadoAprendizaje'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'normativa', ['Contenido'])

        # Adding model 'SubContenido'
        db.create_table(u'normativa_subcontenido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contenido', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['normativa.Contenido'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'normativa', ['SubContenido'])

        # Adding model 'Grupo'
        db.create_table(u'normativa_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'normativa', ['Grupo'])

        # Adding model 'Evaluacion'
        db.create_table(u'normativa_evaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'normativa', ['Evaluacion'])


    def backwards(self, orm):
        # Deleting model 'Competencia'
        db.delete_table(u'normativa_competencia')

        # Deleting model 'Objetivo'
        db.delete_table(u'normativa_objetivo')

        # Deleting model 'Materia'
        db.delete_table(u'normativa_materia')

        # Removing M2M table for field competencias on 'Materia'
        db.delete_table(db.shorten_name(u'normativa_materia_competencias'))

        # Removing M2M table for field objetivos on 'Materia'
        db.delete_table(db.shorten_name(u'normativa_materia_objetivos'))

        # Deleting model 'ResultadoAprendizaje'
        db.delete_table(u'normativa_resultadoaprendizaje')

        # Deleting model 'CriterioEvaluacion'
        db.delete_table(u'normativa_criterioevaluacion')

        # Deleting model 'Contenido'
        db.delete_table(u'normativa_contenido')

        # Deleting model 'SubContenido'
        db.delete_table(u'normativa_subcontenido')

        # Deleting model 'Grupo'
        db.delete_table(u'normativa_grupo')

        # Deleting model 'Evaluacion'
        db.delete_table(u'normativa_evaluacion')


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
            'Meta': {'ordering': "['resultadoAprendizaje']", 'object_name': 'CriterioEvaluacion'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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