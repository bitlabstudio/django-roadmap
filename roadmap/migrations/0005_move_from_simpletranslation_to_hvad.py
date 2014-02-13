# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for milestonetrans in orm['roadmap.MilestoneTranslationRenamed'].objects.all():
            orm['roadmap.MilestoneTranslation'].objects.create(
                master=milestonetrans.milestone,
                language_code=milestonetrans.language,
                name=milestonetrans.name,
            )

        for eventtrans in orm['roadmap.EventTranslationRenamed'].objects.all():
            orm['roadmap.EventTranslation'].objects.create(
                master=eventtrans.event,
                language_code=eventtrans.language,
                title=eventtrans.title,
                description=eventtrans.description,
            )

    def backwards(self, orm):
        pass

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
    symmetrical = True
