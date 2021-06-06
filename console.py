import pdb
from models.session import Session
from models.member import Member
from models.member_session import Member_Session

import repositories.session_repository as session_repository
import repositories.member_repository as member_repository
import repositories.member_session_repository as member_session_repository

member_session_repository.delete_all()
session_repository.delete_all()
member_repository.delete_all()

member1 = Member("Mohammad", "Ali")
member_repository.save(member1)

session1 = Session("Booty Pump", 30)
session_repository.save(session1)

member_session1 = Member_Session(member1, session1, "Couldn't sit for a week!")
member_session_repository.save(member_session1)

pdb.set_trace()
