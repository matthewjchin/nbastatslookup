import unittest
import app
from flask import Response
from nba_api.stats.static import players


class MyTestCase(unittest.TestCase):
    def test_app(self):
        self.assertIsNotNone(self, Response.status_code)

    def test_tonight_games(self):
        self.assertIsNotNone(app.get_tonight_games())

    # def test_get_active_player(self):
    #     all_players = players.get_players()
    #
    #     self.assertIsNotNone(app.get_active_player())

    def test_main(self):
        self.assertIsNotNone(app.main())


if __name__ == '__main__':
    unittest.main()
