# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Search'
        db.create_table('djbeagle_search', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('djbeagle', ['Search'])

        # Adding M2M table for field criteria on 'Search'
        db.create_table('djbeagle_search_criteria', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('search', models.ForeignKey(orm['djbeagle.search'], null=False)),
            ('criterion', models.ForeignKey(orm['djbeagle.criterion'], null=False))
        ))
        db.create_unique('djbeagle_search_criteria', ['search_id', 'criterion_id'])

        # Adding M2M table for field articles on 'Search'
        db.create_table('djbeagle_search_articles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('search', models.ForeignKey(orm['djbeagle.search'], null=False)),
            ('article', models.ForeignKey(orm['djbeagle.article'], null=False))
        ))
        db.create_unique('djbeagle_search_articles', ['search_id', 'article_id'])

        # Adding M2M table for field engines on 'Search'
        db.create_table('djbeagle_search_engines', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('search', models.ForeignKey(orm['djbeagle.search'], null=False)),
            ('engine', models.ForeignKey(orm['djbeagle.engine'], null=False))
        ))
        db.create_unique('djbeagle_search_engines', ['search_id', 'engine_id'])

        # Adding model 'Criterion'
        db.create_table('djbeagle_criterion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search_string', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('djbeagle', ['Criterion'])

        # Adding model 'Article'
        db.create_table('djbeagle_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('year', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('authors', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('publication', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('engine', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('djbeagle', ['Article'])

        # Adding model 'Engine'
        db.create_table('djbeagle_engine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('djbeagle', ['Engine'])


    def backwards(self, orm):
        # Deleting model 'Search'
        db.delete_table('djbeagle_search')

        # Removing M2M table for field criteria on 'Search'
        db.delete_table('djbeagle_search_criteria')

        # Removing M2M table for field articles on 'Search'
        db.delete_table('djbeagle_search_articles')

        # Removing M2M table for field engines on 'Search'
        db.delete_table('djbeagle_search_engines')

        # Deleting model 'Criterion'
        db.delete_table('djbeagle_criterion')

        # Deleting model 'Article'
        db.delete_table('djbeagle_article')

        # Deleting model 'Engine'
        db.delete_table('djbeagle_engine')


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
        'djbeagle.article': {
            'Meta': {'object_name': 'Article'},
            'authors': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'engine': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'publication': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'djbeagle.criterion': {
            'Meta': {'object_name': 'Criterion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'search_string': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'djbeagle.engine': {
            'Meta': {'object_name': 'Engine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'djbeagle.search': {
            'Meta': {'object_name': 'Search'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['djbeagle.Article']", 'symmetrical': 'False', 'blank': 'True'}),
            'criteria': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['djbeagle.Criterion']", 'symmetrical': 'False', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'engines': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['djbeagle.Engine']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['djbeagle']