# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'event_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('organizer', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, blank=True)),
            ('start_hour', self.gf('django.db.models.fields.TimeField')(default=datetime.time(1, 26, 49, 342954))),
            ('end_hour', self.gf('django.db.models.fields.TimeField')(default=datetime.time(1, 26, 49, 342991))),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('likes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'event', ['Event'])

        # Adding model 'Speaker'
        db.create_table(u'event_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'event', ['Speaker'])

        # Adding model 'Topic'
        db.create_table(u'event_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Event'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('start_hour', self.gf('django.db.models.fields.TimeField')(default=datetime.time(1, 26, 49, 344348))),
            ('end_hour', self.gf('django.db.models.fields.TimeField')(default=datetime.time(1, 26, 49, 344376))),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('likes', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Speaker'])),
        ))
        db.send_create_signal(u'event', ['Topic'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'event_event')

        # Deleting model 'Speaker'
        db.delete_table(u'event_speaker')

        # Deleting model 'Topic'
        db.delete_table(u'event_topic')


    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 26, 49, 342991)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 26, 49, 342954)'}),
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
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 26, 49, 344376)'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Speaker']"}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 26, 49, 344348)'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['event']