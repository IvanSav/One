from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    url(r'^articles/all/$', 'oneapp.views.articles'),
    url(r'^articles/example/(?P<article_id>\d+)/$', 'oneapp.views.example'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'oneapp.views.article'),
    url(r'^articles/addorder/(?P<article_id>\d+)/$', 'oneapp.views.addorder'),
    url(r'^', 'oneapp.views.articles'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}), 
)
