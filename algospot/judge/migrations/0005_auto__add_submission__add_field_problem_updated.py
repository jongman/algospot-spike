# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Submission'
        db.create_table('judge_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submitted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('problem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['judge.Problem'], null=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='', max_length=64)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('length', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('source', self.gf('django.db.models.fields.TextField')(default='')),
            ('message', self.gf('django.db.models.fields.TextField')(null=True)),
            ('time', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('memory', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('judge', ['Submission'])

        # Adding field 'Problem.updated'
        db.add_column('judge_problem', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, db_index=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Submission'
        db.delete_table('judge_submission')

        # Deleting field 'Problem.updated'
        db.delete_column('judge_problem', 'updated')


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
            'time_limit': ('django.db.models.fields.IntegerField', [], {'default': '10000'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'judge.submission': {
            'Meta': {'object_name': 'Submission'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'memory': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['judge.Problem']", 'null': 'True'}),
            'source': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'submitted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['judge']
