import unittest
from src import app
from flask import Response
from nba_api.stats.static import players


class MyTestCase(unittest.TestCase):
    def test_app(self):
        self.assertIsNotNone(self, Response.status_code)

    def test_tonight_games(self):
        self.assertIsNotNone(app.get_tonight_games())

    def test_get_any_player(self):
        players_list = players.get_players()
        player_info = players_list[200]
        self.assertIsNotNone(player_info)

    def test_get_active_player(self):
        nba_player = players.find_players_by_full_name("hello there")
        self.assertFalse(nba_player)
        nba_player = players.find_players_by_full_name("Stephen Curry")
        self.assertTrue(nba_player)

    def test_main(self):
        self.assertIsNotNone(app.main())


if __name__ == '__main__':
    unittest.main()
