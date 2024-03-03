import unittest
import get_player_data
from nba_api.stats.static import players


class MyTestCase(unittest.TestCase):
    def test_get_player_name(self):
        # active = players.get_active_players()
        self.assertIsNotNone(get_player_data.get_player_name(0))
        self.assertIsNotNone(get_player_data.get_player_name(3))
        self.assertIsNotNone(get_player_data.get_player_name(79))
        self.assertIsNotNone(get_player_data.get_player_name(120))
        self.assertIsNotNone(get_player_data.get_player_name(400))




if __name__ == '__main__':
    unittest.main()
