from db.run_sql import run_sql
from models.member_class import Member_Class
import repositories.member_repository as member_repository
import repositories.class_repository as class_repository

def save(member_class):
    sql = "INSERT INTO member_classes( member_id, classes_id, review ) VALUES (%s, %s, %s) RETURNING id"
    values = [member_class.member.id, member_class.classes.id, member_class.review]
    results = run_sql(sql, values)
    member_class.id = results[0]['id']
    return member_class

def select_all():
    member_classes = []

    sql = "SELECT * FROM member_classes"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        classes = class_repository.select(row['classes_id'])
        member_class = Member_Class(member, classes, row['review'], row['id'])
        member_classes.append(member_class)
    return member_classes

def delete_all():
    sql = "DELETE FROM member_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM member_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)