# -*- coding: utf-8 -*-
from tastypie.api import Api
from apps.character.resources import CharacterResource
from apps.history.resources import HistoryResource

api = Api(api_name=u'v1')


def get_api_container():
    return api


api.register(CharacterResource())
api.register(HistoryResource())
