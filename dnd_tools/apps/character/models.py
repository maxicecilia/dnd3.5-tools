import math
from mongoengine import (
    Document, EmbeddedDocument, EmbeddedDocumentField,
    BooleanField, IntField, ListField, StringField, )

# Attribute constantes
ATTRIBUTES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
STR = 0
DEX = 1
CON = 2
INT = 3
WIS = 4
CHA = 5


class ArmorClass(EmbeddedDocument):
    armor = IntField(default=0)
    shield = IntField(default=0)
    natural = IntField(default=0)
    deflect = IntField(default=0)
    other = IntField(default=0)

    def surprise(self):
        return self.armor + self.natural + self.deflect + self.other

    def total(self):
        return self.armor + self.shield + self.natural + self.deflect + self.other

    def __unicode__(self):
        return "AC: Armor:%s, Shield:%s, Nat:%s, Deflect:%s, Other:%s" % (self.armor, self.shield, self.natural, self.deflect, self.other)


class HitPoints(EmbeddedDocument):
    total = IntField(default=0)
    current = IntField(default=0)
    temp_damage = IntField(default=0)
    hit_dice = StringField(max_length=255)
    damage_reduction = StringField(max_length=255, required=False)

    def __unicode__(self):
        return "%s/%s" % (self.current, self.total)


class CharacterClass(EmbeddedDocument):
    name = StringField(max_length=80)
    short_name = StringField(max_length=10)
    level = IntField(default=0)


class SavingThrows(EmbeddedDocument):
    name = StringField(max_length=30)
    base_value = IntField(default=0)
    misc_mod = IntField(default=0)
    temp_mod = IntField(default=0)

    def get_total(self):
        return self.base_value + self.misc_mod + self.temp_mod


class Attribute(EmbeddedDocument):
    name = StringField(max_length=15)
    value = IntField(default=0)
    temp_mod = IntField(default=0)

    def get_mod_score(self):
        return math.floor(self.value - 10) / 2

    def current_score(self):
        return self.value + self.temp_mod

    def __unicode__(self):
        return "%s: %s" % (self.name, self.current_score())


class Character(Document):
    '''
        Player character data model.

        [initiative_mod]: Misc initiative modificator. This add with dex bonus.

        { "player_name" : "maxi",
            "name" : "Thank",
            "ecl" : 13,
            "race" : "semiorco",
            "alignment" : "Neutral",
            "size" : "M",
            "active" : true,
            "initiative_mod" : 4,
            "classes" : [
                { "name" : "Explorador", "short_name" : "Exp", "level" : 9 },
                { "name" : "Guerrero", "short_name" : "Gue", "value" : 2 },
                { "name" : "Heredero De Siberys", "short_name" : "HdS", "value" : 2 }
            ],
            "attributes" : [
                { "name" : "STR", "value" : 21, "temp_mod" : 0 },
                { "name" : "DEX", "value" : 18, "temp_mod" : 0 },
                { "name" : "CON", "value" : 14, "temp_mod" : 0 },
                { "name" : "INT", "value" : 10, "temp_mod" : 0 },
                { "name" : "WIS", "value" : 12, "temp_mod" : 0 },
                { "name" : "CHA", "value" : 9, "temp_mod" : 0 }
            ],
            "saving_throws" : [
                { "name" : "FORTITUDE", "base_value" : 12,"misc_mod" : 0, "temp_mod" : 0 },
                { "name" : "REFLEX", "base_value" : 9, "misc_mod" : 0, "temp_mod" : 0},
                { "name" : "WILL", "base_value" : 6, "misc_mod" : 0, "temp_mod" : 0}
            ],
            "armor_class" : {
                "armor" = 8,
                "shield" = 4,
                "natural" = 0,
                "deflect" = 0,
                "other" = 0
            },
            "hit_points" : {
                "total" : 110,
                "current" : 110,
                "hit_dice" : "d6"
            }
        }

    '''
    player_name = StringField(max_length=255)
    name = StringField(max_length=255)
    alignment = StringField(max_length=255)
    classes = ListField(EmbeddedDocumentField(CharacterClass))
    ecl = IntField(default=0)
    size = StringField(max_length=1)
    race = StringField(max_length=255)
    attributes = ListField(EmbeddedDocumentField(Attribute))
    hit_points = EmbeddedDocumentField(HitPoints)
    armor_class = EmbeddedDocumentField(ArmorClass)
    initiative_mod = IntField(default=0)
    saving_throws = ListField(EmbeddedDocumentField(SavingThrows))

    # Non-game attributes
    active = BooleanField(default=True)

    @property
    def dex(self):
        #return [foo for foo in self.attributes if foo.name == ATTRIBUTES[DEX]][0]
        return self.attributes[DEX]

    @property
    def armor_class_full(self):
        return int(10 + self.armor_class.total() + self.dex.get_mod_score())

    @property
    def armor_class_touch(self):
        return int(10 + self.dex.get_mod_score())

    @property
    def armor_class_flanked(self):
        return int(10 + self.armor_class.surprise())

    def load(self):
        self.load_initiative()

    def load_initiative(self):
        '''
            TODO: Fix.
        '''
        self.initiative = self.initiative_mod + self.dex.get_mod_score()
