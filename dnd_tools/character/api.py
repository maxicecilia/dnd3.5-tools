# -*- coding: utf-8 -*-
from tastypie.api import Api
from character.resources import CharacterResource

api = Api(api_name=u'v1')


def get_api_container():
    return api


api.register(CharacterResource())
