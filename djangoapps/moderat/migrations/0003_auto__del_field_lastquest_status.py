# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Lastquest.status'
        db.delete_column(u'moderat_lastquest', 'status')


    def backwards(self, orm):
        # Adding field 'Lastquest.status'
        db.add_column(u'moderat_lastquest', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(23, 11, 19, 640929)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(23, 11, 19, 640892)'}),
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
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(23, 11, 19, 642298)'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Speaker']"}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(23, 11, 19, 642271)'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
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