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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('iduser', self.gf('django.db.models.fields.IntegerField')()),
            ('idthema', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'inev', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'inev_question')


    models = {
        u'inev.question': {
            'Meta': {'object_name': 'Question'},
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idthema': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'iduser': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['inev']