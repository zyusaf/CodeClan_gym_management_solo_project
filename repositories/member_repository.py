from db.run_sql import run_sql
from models.session import Session
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.id]
    run_sql(sql, values)

def sessions(member):
    sessions = []

    sql = "SELECT sessions.* FROM sessions INNER JOIN member_sessions ON member_sessions.session_id = sessions.id WHERE member_id =%s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        session = Session(row['description'], row['duration'], row['id'])
        sessions.append(session)
    
    return sessions