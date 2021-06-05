from db.run_sql import run_sql
from models.classes import Classes

def save(class1):
    sql = "INSERT INTO classes(description, duration) VALUES (%s, %s) RETURNING id"
    values = [class1.description, class1.duration]
    results = run_sql(sql, values)
    class1.id = results[0]['id']
    return class1

def select_all():
    classes = []

    sql = "SELECT * FROM classes"
    results = run_sql(sql)

    for row in results:
        class1 = Classes(row['description'], row['duration'])
        classes.append(class1)
    return classes