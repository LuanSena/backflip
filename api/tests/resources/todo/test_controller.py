import unittest
from flask import json

from api.app import app


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(json.loads(response.get_data()), {'hello': 'world'})


if __name__ == "__main__":
    unittest.main()
