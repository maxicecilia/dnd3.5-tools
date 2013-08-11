from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from character.models import Character

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home', name='home'),

    url(r'^character$', 'character.views.get_all_characters', name="all_chars"),

    url(r'^character/(?P<name>\w*)/$', 'character.views.get_characters_by_name', name="char_by_name"),

    # url(r'^dnd_tools/', include('dnd_tools.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
