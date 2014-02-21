from tastypie import authorization
from tastypie import fields as tastypie_fields
from tastypie_mongoengine import resources, fields
from .models import Character, HitPoints, Attribute, ArmorClass


class AttributeResource(resources.MongoEngineResource):
    class Meta:
        object_class = Attribute


class HitPointsResource(resources.MongoEngineResource):
    class Meta:
        object_class = HitPoints


class ArmorClassResource(resources.MongoEngineResource):

    class Meta:
        object_class = ArmorClass


class CharacterResource(resources.MongoEngineResource):
    hit_points = fields.EmbeddedDocumentField(embedded='apps.character.resources.HitPointsResource', attribute='hit_points')
    armor_class = fields.EmbeddedDocumentField(embedded='apps.character.resources.ArmorClassResource', attribute='armor_class')
    attributes = fields.EmbeddedListField(of='apps.character.resources.AttributeResource', attribute='attributes', full=True, null=True)

    armor_class_full = tastypie_fields.CharField(attribute='armor_class_full')
    armor_class_touch = tastypie_fields.CharField(attribute='armor_class_touch')
    armor_class_flanked = tastypie_fields.CharField(attribute='armor_class_flanked')

    class Meta:
        queryset = Character.objects.all()
        allowed_methods = ('get', 'post', 'put', 'delete', 'patch')
        authorization = authorization.Authorization()
        excludes = ['active', 'classes', ]
