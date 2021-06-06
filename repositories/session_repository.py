from db.run_sql import run_sql
from models.member import Member
from models.session import Session

def save(session):
    sql = "INSERT INTO sessions(description, duration) VALUES (%s, %s) RETURNING id"
    values = [session.description, session.duration]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        session = Session(row['description'], row['duration'])
        sessions.append(session)
    return sessions

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result['description'], result['duration'])
    return session

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(session):
    sql =  "UPDATE sessions SET (description, duration) = (%s, %s) WHERE id = %s"
    values = [session.description, session.duration, session.id]
    run_sql(sql, values)

def members(session):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN member_sessions ON member_sessions.member_id = members id WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], ['last_name'], row['id'])
        members.append(member)
    
    return members