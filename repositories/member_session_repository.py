from db.run_sql import run_sql
from models.member_session import Member_Session
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

def save(member_session):
    sql = "INSERT INTO member_sessions( member_id, session_id, review ) VALUES (%s, %s, %s) RETURNING id"
    values = [member_session.member.id, member_session.session.id, member_session.review]
    results = run_sql(sql, values)
    member_session.id = results[0]['id']
    return member_session

def select_all():
    member_sessions = []

    sql = "SELECT * FROM member_sessions"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        session = session_repository.select(row['session_id'])
        member_session = Member_Session(member, session, row['review'], row['id'])
        member_sessions.append(member_session)
    return member_sessions

def delete_all():
    sql = "DELETE FROM member_sessions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM member_sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)