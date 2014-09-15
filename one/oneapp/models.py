from django.db import models
from time import time
# Create your models here.

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Article(models.Model):
    class Meta():
            db_table = 'article'    
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_image = models.FileField(upload_to=get_upload_file_name)    