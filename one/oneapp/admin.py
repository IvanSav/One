from django.contrib import admin
from oneapp.models import Article, Order


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
              'article_title',
              'article_text',
              'article_date',
              'image_img',
            )    
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(Order)