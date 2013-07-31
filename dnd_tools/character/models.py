from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class ArmorClass(models.Model):
    armor = models.IntegerField(default=0)
    shield = models.IntegerField(default=0)
    dex = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    natural = models.IntegerField(default=0)
    deflect = models.IntegerField(default=0)
    other = models.IntegerField(default=0)

    def get_armor_class_full(self):
        return 10 + self.armor + self.shield + self.dex + self.size + self.natural + self.deflect + self.other

    def get_armor_class_touch(self):
        return 10 + self.dex + self.size + self.deflect + self.other

    def get_armor_class_flat_footed(self):
        return self.get_armor_class_full() - self.dex


class HitPoints(models.Model):
    total = models.IntegerField(default=0)
    current = models.IntegerField(default=0)
    hit_dice = models.CharField(max_length=255)
    damage_reduction = models.CharField(max_length=255)

class Character(models.Model):
    '''
        {
            "_id" : ObjectId("51f88d34f398b679ab3bb4ca"),
            "race" : "",
            "player_name" : "Maxi",
            "name" : "Kodax",
            "created_at" : ISODate("2013-07-30T23:06:12.956Z"),
            "ecl" : 0,
            "experience" : [ ],
            "saving_throws" : [ ],
            "classes" : [
                {
                    "lvl" : 14,
                    "name" : "Picaro"
                }
            ],
            "initiative" : [ ],
            "hit_points" : [ ],
            "active" : true,
            "attributes" : [ ],
            "armor_class" : [ ],
            "alignment" : "NM",
            "size" : ""
        }

    '''
    player_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    alignment = models.CharField(max_length=255)
    # current, next_level
    experience = ListField()
    # name, lvl
    classes = ListField()
    ecl = models.IntegerField(default=0)
    size = models.CharField(max_length=1)
    race = models.CharField(max_length=255)
    # str (score, object_score, temp_score), dex, con, int wis, cha
    attributes = ListField()
    hit_points = EmbeddedModelField('HitPoints')
    armor_class = EmbeddedModelField('ArmorClass')
    initiative = ListField()
    saving_throws = ListField()

    # Non-game attributes
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
