# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.db import models
from sorl.thumbnail.shortcuts import get_thumbnail
from datetime import date, time, datetime
import datetime
import PIL
# Create your models here.

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Article(models.Model):
    class Meta():
            db_table = 'article'
            verbose_name = 'Костюм'
            verbose_name_plural = 'Костюмы'                       
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_image = models.FileField(upload_to=get_upload_file_name)
    
    def image_img(self):
        if self.article_image:
            return u'<img src="%s" width="100"/>' % self.article_image.url
        else:
            return '(none)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True    
        
    
    
                 
    def __unicode__(self):
            return self.article_title    
        
class Order(models.Model):
    class Meta():
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'        
    order_title = models.CharField(max_length=200, blank=False, default=str(datetime.datetime.now()))
    order_date = models.DateTimeField(blank=False, default=datetime.datetime.now)
    order_phone = models.CharField(max_length=200)
    order_article = models.ForeignKey(Article, blank=True, null=True)
    def __unicode__(self):
                return self.order_title     