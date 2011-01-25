# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Problem.key'
        db.add_column('judge_problem', 'key', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=64), keep_default=False)

        # Adding field 'Problem.author'
        db.add_column('judge_problem', 'author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True), keep_default=False)

        # Adding field 'Problem.source'
        db.add_column('judge_problem', 'source', self.gf('django.db.models.fields.CharField')(max_length=128, null=True), keep_default=False)

        # Adding field 'Problem.input'
        db.add_column('judge_problem', 'input', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Problem.output'
        db.add_column('judge_problem', 'output', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Problem.sample_input'
        db.add_column('judge_problem', 'sample_input', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Problem.sample_output'
        db.add_column('judge_problem', 'sample_output', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Problem.note'
        db.add_column('judge_problem', 'note', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Problem.judge_module'
        db.add_column('judge_problem', 'judge_module', self.gf('django.db.models.fields.CharField')(default='', max_length=128), keep_default=False)

        # Adding field 'Problem.time_limit'
        db.add_column('judge_problem', 'time_limit', self.gf('django.db.models.fields.IntegerField')(default=10000), keep_default=False)

        # Adding field 'Problem.memory_limit'
        db.add_column('judge_problem', 'memory_limit', self.gf('django.db.models.fields.IntegerField')(default=65536), keep_default=False)

        # Adding field 'Problem.accepted'
        db.add_column('judge_problem', 'accepted', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Problem.submissions'
        db.add_column('judge_problem', 'submissions', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Problem.key'
        db.delete_column('judge_problem', 'key')

        # Deleting field 'Problem.author'
        db.delete_column('judge_problem', 'author_id')

        # Deleting field 'Problem.source'
        db.delete_column('judge_problem', 'source')

        # Deleting field 'Problem.input'
        db.delete_column('judge_problem', 'input')

        # Deleting field 'Problem.output'
        db.delete_column('judge_problem', 'output')

        # Deleting field 'Problem.sample_input'
        db.delete_column('judge_problem', 'sample_input')

        # Deleting field 'Problem.sample_output'
        db.delete_column('judge_problem', 'sample_output')

        # Deleting field 'Problem.note'
        db.delete_column('judge_problem', 'note')

        # Deleting field 'Problem.judge_module'
        db.delete_column('judge_problem', 'judge_module')

        # Deleting field 'Problem.time_limit'
        db.delete_column('judge_problem', 'time_limit')

        # Deleting field 'Problem.memory_limit'
        db.delete_column('judge_problem', 'memory_limit')

        # Deleting field 'Problem.accepted'
        db.delete_column('judge_problem', 'accepted')

        # Deleting field 'Problem.submissions'
        db.delete_column('judge_problem', 'submissions')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'judge.problem': {
            'Meta': {'object_name': 'Problem'},
            'accepted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'judge_module': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '64'}),
            'memory_limit': ('django.db.models.fields.IntegerField', [], {'default': '65536'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'note': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'output': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'sample_input': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'sample_output': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'submissions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'time_limit': ('django.db.models.fields.IntegerField', [], {'default': '10000'})
        }
    }

    complete_apps = ['judge']
