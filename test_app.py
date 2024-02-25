import unittest
from app import get_player_name_active


class MyTestCase(unittest.TestCase):
    def test_get_player_name_active(self):
        self.assertFalse(get_player_name_active())
        self.assertFalse(get_player_name_active(""))


if __name__ == '__main__':
    unittest.main()
