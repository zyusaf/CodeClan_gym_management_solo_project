import unittest
from models.member_class import Member_Class

class TestMember_Class(unittest.TestCase):
    def setUp(self):
        self.member_class = Member_Class("John Wayne", "Booty Pump", "Was ok")

    def test_member_class_has_member(self):
        self.assertEqual("John Wayne", self.member_class.member)

    def test_member_class_has_class(self):
        self.assertEqual("Booty Pump", self.member_class.classes)

    def test_member_class_has_review(self):
        self.assertEqual("Was ok", self.member_class.review)