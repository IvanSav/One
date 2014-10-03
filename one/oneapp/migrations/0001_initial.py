# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table('article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('article_text', self.gf('django.db.models.fields.TextField')()),
            ('article_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('article_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'oneapp', ['Article'])

        # Adding model 'Order'
        db.create_table('order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('order_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('order_phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'oneapp', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table('article')

        # Deleting model 'Order'
        db.delete_table('order')


    models = {
        u'oneapp.article': {
            'Meta': {'object_name': 'Article', 'db_table': "'article'"},
            'article_date': ('django.db.models.fields.DateTimeField', [], {}),
            'article_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'article_text': ('django.db.models.fields.TextField', [], {}),
            'article_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'oneapp.order': {
            'Meta': {'object_name': 'Order', 'db_table': "'order'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'order_phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['oneapp']