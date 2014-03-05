# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Press'
        db.create_table(u'press_press', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'press', ['Press'])

        # Adding model 'Image'
        db.create_table(u'press_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('press', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['press.Press'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('set_to_preview', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'press', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Press'
        db.delete_table(u'press_press')

        # Deleting model 'Image'
        db.delete_table(u'press_image')


    models = {
        u'press.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'press': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['press.Press']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'set_to_preview': ('django.db.models.fields.BooleanField', [], {})
        },
        u'press.press': {
            'Meta': {'object_name': 'Press'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['press']