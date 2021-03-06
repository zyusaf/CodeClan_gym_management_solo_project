from itertools import filterfalse
from models.member_session import Member_Session
from repositories import member_session_repository, session_repository
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
from itertools import filterfalse

members_blueprint = Blueprint("members", __name__)

# #INDEX
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

#NEW
@members_blueprint.route("/members/new")
def new_member():
    members = member_repository.select_all()
    return render_template("members/new.html", members = members)

#CREATE
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    new_member = Member(first_name, last_name)
    member_repository.save(new_member)
    return redirect("/members")

#EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member)

#UPDATE
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    member = Member(first_name, last_name, id)
    member_repository.update(member)
    return redirect("/members")

#DELETE
@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members')

@members_blueprint.route("/members/<member_id>/add_session", methods=['POST'])
def add_session_to_member(member_id):
    member = member_repository.select(member_id)
    session = session_repository.select(request.form["session_id"])
    member_session = Member_Session(member, session, "")
    member_session_repository.save(member_session)

    return redirect(f"/members/{member_id}")

#SHOW
@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    sessions = member_repository.sessions(member)
    all_sessions = session_repository.select_all()
    assignable_sessions = [x for x in filterfalse(lambda m: m.id in [session.id for session in sessions], all_sessions)]

    return render_template("members/show.html", member = member, sessions = sessions, assignable_sessions = assignable_sessions)