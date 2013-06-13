# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LinkCategory'
        db.create_table(u'links_linkcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'links', ['LinkCategory'])

        # Adding model 'LinkItem'
        db.create_table(u'links_linkitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['links.LinkCategory'])),
            ('resource_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('resource_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('resource_description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'links', ['LinkItem'])


    def backwards(self, orm):
        # Deleting model 'LinkCategory'
        db.delete_table(u'links_linkcategory')

        # Deleting model 'LinkItem'
        db.delete_table(u'links_linkitem')


    models = {
        u'links.linkcategory': {
            'Meta': {'object_name': 'LinkCategory'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'links.linkitem': {
            'Meta': {'object_name': 'LinkItem'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['links.LinkCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'resource_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'resource_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'resource_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['links']