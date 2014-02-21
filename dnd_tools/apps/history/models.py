import datetime
from mongoengine.django.auth import User
from mongoengine import (
    Document, EmbeddedDocument, EmbeddedDocumentField,
    BooleanField, DateTimeField, ListField, ReferenceField, StringField)


class HistoryEntry(EmbeddedDocument):
    '''
    '''
    date_posted = DateTimeField(default=datetime.datetime.now())
    text = StringField(max_length=500, required=True)
    user = ListField(ReferenceField(User))


class History(Document):
    '''
    '''
    owner = ReferenceField(User)
    active = BooleanField(default=True)
    date_created = DateTimeField(default=datetime.datetime.now())
    entries = ListField(EmbeddedDocumentField(HistoryEntry))
