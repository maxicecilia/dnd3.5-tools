from django.conf.urls import patterns, url, include
from apps.website.api import get_api_container
from django.views.generic import TemplateView

#from django.contrib import admin
#admin.autodiscover()
#from mongoadmin import site

urlpatterns = patterns(
    '',
    # Website URLs
    url(r'^$', 'apps.website.views.home', name='home'),
    url(r'^character_room/$', 'apps.website.views.character_room_index', name='character_room_index'),
    url(r'^character$', 'apps.character.views.get_all_characters', name="all_chars"),
    url(r'^character/(?P<name>\w*)/$', 'apps.character.views.get_characters_by_name', name="char_by_name"),

    # Tastypie URLs
    url(r'^api/', include(get_api_container().urls)),

    # New access point with AngularJS
    url(r'^rooms/$', TemplateView.as_view(template_name="new_index.html")),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(site.urls)),
)
