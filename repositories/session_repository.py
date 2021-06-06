from db.run_sql import run_sql
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