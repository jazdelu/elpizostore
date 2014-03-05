# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Collection'
        db.create_table(u'collection_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'collection', ['Collection'])

        # Adding model 'Lookbook'
        db.create_table(u'collection_lookbook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection.Collection'])),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('set_to_cover', self.gf('django.db.models.fields.BooleanField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'collection', ['Lookbook'])


    def backwards(self, orm):
        # Deleting model 'Collection'
        db.delete_table(u'collection_collection')

        # Deleting model 'Lookbook'
        db.delete_table(u'collection_lookbook')


    models = {
        u'collection.collection': {
            'Meta': {'object_name': 'Collection'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'collection.lookbook': {
            'Meta': {'object_name': 'Lookbook'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collection.Collection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'set_to_cover': ('django.db.models.fields.BooleanField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['collection']