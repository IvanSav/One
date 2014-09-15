from django.conf.urls import patterns, include, url
from django.conf.urls.static import static



urlpatterns = patterns('',
    url(r'^articles/all/$', 'oneapp.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'oneapp.views.article'),
    url(r'^', 'oneapp.views.articles'),
)
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )