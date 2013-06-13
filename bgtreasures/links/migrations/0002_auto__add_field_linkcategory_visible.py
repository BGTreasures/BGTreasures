# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LinkCategory.visible'
        db.add_column(u'links_linkcategory', 'visible',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LinkCategory.visible'
        db.delete_column(u'links_linkcategory', 'visible')


    models = {
        u'links.linkcategory': {
            'Meta': {'object_name': 'LinkCategory'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
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