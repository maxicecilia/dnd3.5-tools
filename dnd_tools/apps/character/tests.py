"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from .models import Character, Attribute, SavingThrows, Initiative
from django.test import TestCase


class SimpleTest(TestCase):

    def test_add_character_ok(self):
        """
            "race" : "",
            "player_name" : "Maxi",
            "name" : "Kodax",
            "created_at" : ISODate("2013-07-30T23:06:12.956Z"),
            "ecl" : 0,
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
        """
        try:
            pj = Character(race='elfo', player_name='maxi', name='Kodax', ecl=18)

            attributes = [
                Attribute(name='str', value=15, temp_mod=0),
                Attribute(name='dex', value=15, temp_mod=0),
                Attribute(name='con', value=15, temp_mod=0),
                Attribute(name='int', value=15, temp_mod=0),
                Attribute(name='wis', value=15, temp_mod=0),
                Attribute(name='char', value=15, temp_mod=0)]

            pj.attributes = attributes

            saving_throws = [
                SavingThrows(name='fortitude', base_value=15, misc_mod=0, temp_mod=0),
                SavingThrows(name='reflex', base_value=15, misc_mod=0, temp_mod=0),
                SavingThrows(name='will', base_value=15, misc_mod=0, temp_mod=0), ]

            pj.saving_throws = saving_throws
            pj.initiative = Initiative(dex_mod=4, feat_mod=4, misc_mod=0)
            pj.save()
            self.assertTrue(True)
        except Exception as e:
            self.fail(e)
