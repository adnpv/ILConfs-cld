# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'inev_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['userp.User'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.Topic'])),
        ))
        db.send_create_signal(u'inev', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'inev_question')


    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 27, 16, 574651)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 27, 16, 574613)'}),
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
            'end_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 27, 16, 576018)'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Speaker']"}),
            'start_hour': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(1, 27, 16, 575990)'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'inev.question': {
            'Meta': {'object_name': 'Question'},
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Topic']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userp.User']"})
        },
        u'userp.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'suscrib': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['inev']