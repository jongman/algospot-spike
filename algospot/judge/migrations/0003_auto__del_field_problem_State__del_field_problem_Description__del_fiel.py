# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Problem.State'
        db.delete_column('judge_problem', 'State')

        # Deleting field 'Problem.Description'
        db.delete_column('judge_problem', 'Description')

        # Deleting field 'Problem.Name'
        db.delete_column('judge_problem', 'Name')

        # Adding field 'Problem.name'
        db.add_column('judge_problem', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=128), keep_default=False)

        # Adding field 'Problem.description'
        db.add_column('judge_problem', 'description', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Problem.state'
        db.add_column('judge_problem', 'state', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Problem.State'
        db.add_column('judge_problem', 'State', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Problem.Description'
        raise RuntimeError("Cannot reverse this migration. 'Problem.Description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Problem.Name'
        raise RuntimeError("Cannot reverse this migration. 'Problem.Name' and its values cannot be restored.")

        # Deleting field 'Problem.name'
        db.delete_column('judge_problem', 'name')

        # Deleting field 'Problem.description'
        db.delete_column('judge_problem', 'description')

        # Deleting field 'Problem.state'
        db.delete_column('judge_problem', 'state')


    models = {
        'judge.problem': {
            'Meta': {'object_name': 'Problem'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['judge']
