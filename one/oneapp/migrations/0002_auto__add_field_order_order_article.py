# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.order_article'
        db.add_column('order', 'order_article',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oneapp.Article'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.order_article'
        db.delete_column('order', 'order_article_id')


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
            'order_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oneapp.Article']", 'null': 'True', 'blank': 'True'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'order_phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['oneapp']