# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventTranslation'
        db.create_table('roadmap_eventtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roadmap.Event'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('start_date_text', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('roadmap', ['EventTranslation'])

        # Adding model 'Event'
        db.create_table('roadmap_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('milestone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roadmap.Milestone'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('roadmap', ['Event'])


    def backwards(self, orm):
        # Deleting model 'EventTranslation'
        db.delete_table('roadmap_eventtranslation')

        # Deleting model 'Event'
        db.delete_table('roadmap_event')


    models = {
        'roadmap.event': {
            'Meta': {'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roadmap.Milestone']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'roadmap.eventtranslation': {
            'Meta': {'object_name': 'EventTranslation'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roadmap.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'start_date_text': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'roadmap.milestone': {
            'Meta': {'object_name': 'Milestone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'roadmap.milestonetranslation': {
            'Meta': {'object_name': 'MilestoneTranslation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roadmap.Milestone']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['roadmap']
