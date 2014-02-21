'''
from mongoadmin import site, DocumentAdmin
from character.models import Character


class CharacterAdmin(DocumentAdmin):
    pass


site.register(Character, CharacterAdmin)
'''
