# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FlqSolv'
        db.create_table(u'moderat_flqsolv', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Event'])),
            ('lcho', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['moderat.LastChoice'])),
            ('lque', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['moderat.Lastquest'])),
            ('nchoices', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'moderat', ['FlqSolv'])

        # Deleting field 'Lastquest.event'
        db.delete_column(u'moderat_lastquest', 'event_id')


    def backwards(self, orm):
        # Deleting model 'FlqSolv'
        db.delete_table(u'moderat_flqsolv')

        # Adding field 'Lastquest.event'
        db.add_column(u'moderat_lastquest', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['event.Event']),
                      keep_default=False)


    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(22, 55, 8, 598097)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(22, 55, 8, 598060)'}),
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
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(22, 55, 8, 599483)'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Speaker']"}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(22, 55, 8, 599453)'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'moderat.choice': {
            'Meta': {'object_name': 'Choice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nchoices': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['moderat.Quest']"})
        },
        u'moderat.flqsolv': {
            'Meta': {'object_name': 'FlqSolv'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcho': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['moderat.LastChoice']"}),
            'lque': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['moderat.Lastquest']"}),
            'nchoices': ('django.db.models.fields.IntegerField', [], {})
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