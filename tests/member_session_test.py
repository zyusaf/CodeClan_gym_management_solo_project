import unittest
from models.member_session import Member_Session

class TestMember_Session(unittest.TestCase):
    def setUp(self):
        self.member_session = Member_Session("John Wayne", "Booty Pump", "Was ok")

    def test_member_session_has_member(self):
        self.assertEqual("John Wayne", self.member_session.member)

    def test_member_session_has_session(self):
        self.assertEqual("Booty Pump", self.member_session.session)

    def test_member_session_has_review(self):
        self.assertEqual("Was ok", self.member_session.review)