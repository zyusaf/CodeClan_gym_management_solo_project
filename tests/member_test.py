import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member("Zaki", "Yusaf")

    def test_member_has_first_name(self):
        self.assertEqual("Zaki", self.member.first_name)

    def test_member_has_last_name(self):
        self.assertEqual("Yusaf", self.member.last_name)