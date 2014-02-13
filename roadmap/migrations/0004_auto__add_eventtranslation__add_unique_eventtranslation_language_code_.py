# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventTranslation'
        db.create_table('roadmap_event_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date_text', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['roadmap.Event'])),
        ))
        db.send_create_signal('roadmap', ['EventTranslation'])

        # Adding unique constraint on 'EventTranslation', fields ['language_code', 'master']
        db.create_unique('roadmap_event_translation', ['language_code', 'master_id'])

        # Adding model 'MilestoneTranslation'
        db.create_table('roadmap_milestone_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['roadmap.Milestone'])),
        ))
        db.send_create_signal('roadmap', ['MilestoneTranslation'])

        # Adding unique constraint on 'MilestoneTranslation', fields ['language_code', 'master']
        db.create_unique('roadmap_milestone_translation', ['language_code', 'master_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'MilestoneTranslation', fields ['language_code', 'master']
        db.delete_unique('roadmap_milestone_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'EventTranslation', fields ['language_code', 'master']
        db.delete_unique('roadmap_event_translation', ['language_code', 'master_id'])

        # Deleting model 'EventTranslation'
        db.delete_table('roadmap_event_translation')

        # Deleting model 'MilestoneTranslation'
        db.delete_table('roadmap_milestone_translation')


    models = {
        'roadmap.event': {
            'Meta': {'ordering': "('start_date',)", 'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['roadmap.Milestone']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'roadmap.eventtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'EventTranslation', 'db_table': "'roadmap_event_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['roadmap.Event']"}),
            'start_date_text': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'roadmap.eventtranslationrenamed': {
            'Meta': {'object_name': 'EventTranslationRenamed'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roadmap.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'start_date_text': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'roadmap.milestone': {
            'Meta': {'ordering': "('start_date',)", 'object_name': 'Milestone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'roadmap.milestonetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'MilestoneTranslation', 'db_table': "'roadmap_milestone_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['roadmap.Milestone']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'roadmap.milestonetranslationrenamed': {
            'Meta': {'object_name': 'MilestoneTranslationRenamed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roadmap.Milestone']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['roadmap']
