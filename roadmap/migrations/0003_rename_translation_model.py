# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table(u'roadmap_milestonetranslation', u'roadmap_milestonetranslationrenamed')
        db.rename_table(u'roadmap_eventtranslation', u'roadmap_eventtranslationrenamed')

    def backwards(self, orm):
        db.rename_table(u'roadmap_milestonetranslationrenamed', u'roadmap_milestonetranslation')
        db.rename_table(u'roadmap_eventtranslationrenamed', u'roadmap_eventtranslation')

    models = {
        'roadmap.event': {
            'Meta': {'ordering': "('start_date',)", 'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['roadmap.Milestone']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
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
        'roadmap.milestonetranslationrenamed': {
            'Meta': {'object_name': 'MilestoneTranslationRenamed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roadmap.Milestone']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['roadmap']
