# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.text'
        db.add_column(u'press_image', 'text',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Image.pub_date'
        db.alter_column(u'press_image', 'pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, null=True))
        # Adding field 'Press.pub_date'
        db.add_column(u'press_press', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Image.text'
        db.delete_column(u'press_image', 'text')


        # Changing field 'Image.pub_date'
        db.alter_column(u'press_image', 'pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 3, 0, 0)))
        # Deleting field 'Press.pub_date'
        db.delete_column(u'press_press', 'pub_date')


    models = {
        u'press.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'press': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['press.Press']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'set_to_preview': ('django.db.models.fields.BooleanField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'press.press': {
            'Meta': {'object_name': 'Press'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['press']