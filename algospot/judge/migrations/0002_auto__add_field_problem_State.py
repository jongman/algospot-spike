# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Problem.State'
        db.add_column('judge_problem', 'State', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Problem.State'
        db.delete_column('judge_problem', 'State')


    models = {
        'judge.problem': {
            'Description': ('django.db.models.fields.TextField', [], {}),
            'Meta': {'object_name': 'Problem'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'State': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['judge']
