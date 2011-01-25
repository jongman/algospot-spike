# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Problem'
        db.create_table('judge_problem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('Description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('judge', ['Problem'])


    def backwards(self, orm):
        
        # Deleting model 'Problem'
        db.delete_table('judge_problem')


    models = {
        'judge.problem': {
            'Description': ('django.db.models.fields.TextField', [], {}),
            'Meta': {'object_name': 'Problem'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['judge']
