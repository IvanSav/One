from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
site_media = '/Users/IvanSavickiy/djangoenv/bin/one/static/'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'one.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('oneapp.urls')),
    url(r'^static/?P<path>.*$',  'django.views.static.serve', {'document_root': site_media}),
)
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )