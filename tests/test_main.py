import unittest
from fastapi.testclient import TestClient
from app.main import create_app, session, prepare_db

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = TestClient(self.app)
        self.session = session
        prepare_db(self.session)

    def test_welcome_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to WebScrapper", response.text)

