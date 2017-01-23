import unittest
import unittest.mock

import models.main
from zones.northshire_abbey import NorthshireAbbey, NorthshireValley, NorthshireVineyards


class NorthshireAbbeyTests(unittest.TestCase):
    def setUp(self):
        self.char_mock = unittest.mock.Mock(level=10)
        self.char_mock.has_loaded_script = lambda x: True
        self.char_mock.loaded_script = lambda x: None
        self.char_mock.has_completed_quest = lambda x: False
        self.char_mock.has_killed_monster = lambda x: False
        self.northshire_valley_monster_count = 5
        self.northshire_valley_npc_count = 2
        self.northshire_valley_quest_count = 2
        self.northshire_vineyards_monster_count = 7
        self.northshire_vineyards_npc_count = 0
        self.northshire_vineyards_quest_count = 1

    def test_zone(self):
        zone = NorthshireAbbey(self.char_mock)
        # it should have loaded subzones
        self.assertTrue(zone.loaded_zones['Northshire Valley'], NorthshireValley)
        # these should not have been loaded because we have not gone in there
        self.assertIsNone(zone.loaded_zones['Northshire Vineyards'])
        self.assertIsNone(zone.loaded_zones['A Peculiar Hut'])
        # it should hold the monsters in the current subzone
        self.assertEqual(len(zone.cs_alive_monsters.keys()), self.northshire_valley_monster_count)
        self.assertEqual(len(zone.cs_alive_npcs.keys()), self.northshire_valley_npc_count)
        self.assertEqual(len(zone.cs_available_quests.keys()), self.northshire_valley_quest_count)
        self.assertEqual(zone.curr_subzone, 'Northshire Valley')

    def test_move_player_valid(self):
        """
        Move the player to a valid subzone giving valid values
        """

        zone = NorthshireAbbey(self.char_mock)
        self.assertIsNone(zone.loaded_zones['Northshire Vineyards'])
        start_subzone, go_to_subzone = 'Northshire Valley', 'Northshire Vineyards'
        result = zone.move_player(current_subzone=start_subzone, destination=go_to_subzone, character=self.char_mock)

        self.assertTrue(result)
        # Should have loaded the zone for the first time
        self.assertIsNotNone(zone.loaded_zones['Northshire Vineyards'])
        self.assertTrue(isinstance(zone.loaded_zones['Northshire Vineyards'], NorthshireVineyards))
        # should have loaded the npcs from the new subzone
        self.assertEqual(len(zone.cs_alive_monsters.keys()), self.northshire_vineyards_monster_count)
        self.assertEqual(len(zone.cs_alive_npcs.keys()), self.northshire_vineyards_npc_count)
        self.assertEqual(len(zone.cs_available_quests.keys()), self.northshire_vineyards_quest_count)

        self.assertEqual(zone.curr_subzone, 'Northshire Vineyards')
        pass

if __name__ == '__main__':
    unittest.main()