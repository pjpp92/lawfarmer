from django.conf.urls import patterns, include, url
from main.views import home, article, flatblock
from django.conf import settings
from django.contrib import admin
from flatblocks.views import edit
from django.contrib.auth.decorators import login_required

from filebrowser.sites import site

SLUG = '(?P<slug>.+)'

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^article$', article, name='article'),
    url(r'^about$', flatblock, {'block':'about'}, name='about'),
    url(r'^contact', flatblock, {'block':'contact'}, name='contact'),
    url(r'^author', flatblock, {'block':'author'}, name='author'),

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


