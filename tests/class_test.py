import unittest
from models.classes import Classes

class TestClasses(unittest.TestCase):
    def setUp(self):
        self.class1 = Classes("Cardio", 45)

    def test_class_has_description(self):
        self.assertEqual("Cardio", self.class1.description)

    def test_class_has_duration(self):
        self.assertEqual(45, self.class1.duration)