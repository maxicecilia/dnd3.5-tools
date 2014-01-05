from tastypie import authorization
from tastypie_mongoengine import resources, fields
from history.models import History, HistoryEntry


class EntryResource(resources.MongoEngineResource):
    class Meta:
        object_class = HistoryEntry
        ordering = ['-date_posted', ]


class HistoryResource(resources.MongoEngineResource):
    entries = fields.EmbeddedListField(of='history.resources.EntryResource', attribute='entries', full=True, null=True)

    class Meta:
        queryset = History.objects.all()
        allowed_methods = ('get', 'post', 'put', 'delete', 'patch')
        authorization = authorization.Authorization()
        excludes = ['active', 'classes', ]
