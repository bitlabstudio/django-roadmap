# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Milestone'
        db.create_table('roadmap_milestone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('roadmap', ['Milestone'])

        # Adding model 'MilestoneTranslation'
        db.create_table('roadmap_milestonetranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('milestone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roadmap.Milestone'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('roadmap', ['MilestoneTranslation'])


    def backwards(self, orm):
        # Deleting model 'Milestone'
        db.delete_table('roadmap_milestone')

        # Deleting model 'MilestoneTranslation'
        db.delete_table('roadmap_milestonetranslation')


    models = {
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
