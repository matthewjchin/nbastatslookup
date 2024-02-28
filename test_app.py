import unittest

from flask import Response


class MyTestCase(unittest.TestCase):
    def test_app(self):
        self.assertIsNotNone(self, Response.status_code)


if __name__ == '__main__':
    unittest.main()
