import math
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


# Attribute constantes
ATTRIBUTES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
STR = 0
DEX = 1
CON = 2
INT = 3
WIS = 4
CHA = 5


class ArmorClass(models.Model):
    armor = models.IntegerField(default=0)
    shield = models.IntegerField(default=0)
    natural = models.IntegerField(default=0)
    deflect = models.IntegerField(default=0)
    other = models.IntegerField(default=0)

    def __str__(self):
        return "AC: Armor:%s, Shield:%s, Nat:%s, Deflect:%s, Other:%s" % (self.armor, self.shield, self.natural, self.deflect, self.other)

class HitPoints(models.Model):
    total = models.IntegerField(default=0)
    current = models.IntegerField(default=0)
    hit_dice = models.CharField(max_length=255)
    damage_reduction = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s/%s" % (self.current, self.total)


class CharacterClass(models.Model):
    name = models.CharField(max_length=80)
    short_name = models.CharField(max_length=10)
    level = models.IntegerField()


class SavingThrows(models.Model):
    name = models.CharField(max_length=30)
    base_value = models.IntegerField()
    misc_mod = models.IntegerField()
    temp_mod = models.IntegerField()

    def get_total(self):
        return self.base_value + self.misc_mod + self.temp_mod

class Attribute(models.Model):
    name = models.CharField(max_length=15)
    value = models.IntegerField()
    temp_mod = models.IntegerField(default=0)

    def get_mod_score(self):
        return math.floor(self.value - 10) / 2 


class Character(models.Model):
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
    player_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    alignment = models.CharField(max_length=255)
    classes = ListField(EmbeddedModelField(CharacterClass))
    ecl = models.IntegerField(default=0)
    size = models.CharField(max_length=1)
    race = models.CharField(max_length=255)
    attributes = ListField(EmbeddedModelField(Attribute))
    hit_points = EmbeddedModelField(HitPoints)
    armor_class = EmbeddedModelField(ArmorClass)
    initiative_mod = models.IntegerField(default=0)
    saving_throws = ListField(EmbeddedModelField(SavingThrows))

    # Non-game attributes
    active = models.BooleanField(default=True)

    def load(self):
        self.load_initiative()

    def load_initiative(self):
        '''
            TODO: Fix.
        '''
        self.initiative = self.initiative_mod + self.attributes[DEX].get_mod_score()

    def get_armor_class_full(self):
        '''
            TODO: Fix.
        '''
        return 10 + self.armor + self.shield + self.natural + self.deflect + self.other

    def get_armor_class_touch(self):
        '''
            TODO: Fix.
        '''
        return 10 + self.deflect + self.other

    def get_armor_class_flat_footed(self):
        '''
            TODO: Fix.
        '''
        return self.get_armor_class_full()

