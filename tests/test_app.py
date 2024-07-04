import unittest
from app.main import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_version_endpoint(self):
        response = self.app.get('/version')
        self.assertEqual(response.status_code, 200)
        self.assertIn('version', response.json)
        self.assertIn('build_sha', response.json)
        self.assertIn('description', response.json)

if __name__ == "__main__":
    unittest.main()
