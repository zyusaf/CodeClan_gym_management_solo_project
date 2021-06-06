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

member2 = Member("Rocky", "Balboa")
member_repository.save(member2)

session1 = Session("Booty Pump", 30)
session_repository.save(session1)

session2 = Session("Zumba", 45)
session_repository.save(session2)

member_session1 = Member_Session(member1, session1, "Couldn't sit for a week!")
member_session_repository.save(member_session1)

member_session2 = Member_Session(member2, session2, "Love zumba and the instructor was great")
member_session_repository.save(member_session2)

pdb.set_trace()
