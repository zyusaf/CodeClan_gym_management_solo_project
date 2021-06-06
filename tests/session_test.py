import unittest
from models.session import Session

class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session("Cardio", 45)

    def test_session_has_description(self):
        self.assertEqual("Cardio", self.session.description)

    def test_session_has_duration(self):
        self.assertEqual(45, self.session.duration)