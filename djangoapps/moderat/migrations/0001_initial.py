# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quest'
        db.create_table(u'moderat_quest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Topic'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'moderat', ['Quest'])

        # Adding model 'Choice'
        db.create_table(u'moderat_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nchoices', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('quest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['moderat.Quest'])),
        ))
        db.send_create_signal(u'moderat', ['Choice'])

        # Adding model 'Lastquest'
        db.create_table(u'moderat_lastquest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Event'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'moderat', ['Lastquest'])

        # Adding model 'LastChoice'
        db.create_table(u'moderat_lastchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nchoices', self.gf('django.db.models.fields.IntegerField')()),
            ('lquest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['moderat.Lastquest'])),
        ))
        db.send_create_signal(u'moderat', ['LastChoice'])


    def backwards(self, orm):
        # Deleting model 'Quest'
        db.delete_table(u'moderat_quest')

        # Deleting model 'Choice'
        db.delete_table(u'moderat_choice')

        # Deleting model 'Lastquest'
        db.delete_table(u'moderat_lastquest')

        # Deleting model 'LastChoice'
        db.delete_table(u'moderat_lastchoice')


    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 26, 24, 234155)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 26, 24, 234119)'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'event.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'event.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 26, 24, 235515)'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Speaker']"}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 26, 24, 235487)'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'moderat.choice': {
            'Meta': {'object_name': 'Choice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nchoices': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['moderat.Quest']"})
        },
        u'moderat.lastchoice': {
            'Meta': {'object_name': 'LastChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lquest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['moderat.Lastquest']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nchoices': ('django.db.models.fields.IntegerField', [], {})
        },
        u'moderat.lastquest': {
            'Meta': {'object_name': 'Lastquest'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'moderat.quest': {
            'Meta': {'object_name': 'Quest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Topic']"})
        }
    }

    complete_apps = ['moderat']