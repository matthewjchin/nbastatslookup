import unittest
from src import get_player_data
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


class MyTestCase(unittest.TestCase):
    def test_get_player_name(self):
        self.assertIsNotNone(get_player_data.get_player_name(0))
        self.assertIsNotNone(get_player_data.get_player_name(3))
        self.assertIsNotNone(get_player_data.get_player_name(79))
        self.assertIsNotNone(get_player_data.get_player_name(120))
        self.assertIsNotNone(get_player_data.get_player_name(400))

    def test_get_player_name_active(self):
        player_info = get_player_data.get_player_name(230)
        self.assertIsNotNone(get_player_data.get_player_name_active(player_info))


if __name__ == '__main__':
    unittest.main()
