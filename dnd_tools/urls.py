from django.conf.urls import patterns, url, include
from website.api import get_api_container

#from django.contrib import admin
#admin.autodiscover()

#from mongoadmin import site

urlpatterns = patterns(
    '',
    url(r'^$', 'website.views.home', name='home'),

    url(r'^character$', 'character.views.get_all_characters', name="all_chars"),
    url(r'^character/(?P<name>\w*)/$', 'character.views.get_characters_by_name', name="char_by_name"),

    url(r'^api/', include(get_api_container().urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(site.urls)),
)
