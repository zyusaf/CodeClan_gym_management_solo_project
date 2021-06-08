from models.member_session import Member_Session
from repositories import member_repository, member_session_repository
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository
import sys
from itertools import filterfalse

sessions_blueprint = Blueprint("sessions", __name__)

#INDEX
@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions = sessions)

#NEW
@sessions_blueprint.route("/sessions/new")
def new_session():
    sessions = session_repository.select_all()
    return render_template("sessions/new.html", sessions = sessions)

#CREATE
@sessions_blueprint.route("/sessions", methods=['POST'])
def create_session():
    description = request.form["description"]
    duration = request.form["duration"]
    new_session = Session(description, duration)
    session_repository.save(new_session)
    return redirect("/sessions")

#EDIT
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repository.select(id)
    return render_template("sessions/edit.html", session = session)

#UPDATE
@sessions_blueprint.route("/sessions/<id>", methods=['POST'])
def update_session(id):
    description = request.form["description"]
    duration = request.form["duration"]
    session = Session(description, duration, id)
    session_repository.update(session)

    return redirect("/sessions")

#DELETE
@sessions_blueprint.route("/sessions/<id>/delete", methods=['POST'])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/<session_id>/add_member", methods=['POST'])
def add_member_to_session(session_id):
    session = session_repository.select(session_id)
    member = member_repository.select(request.form["member_id"])
    member_session = Member_Session(member, session, "")
    member_session_repository.save(member_session)
    
    return redirect(f"/sessions/{session_id}")

#SHOW
@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repository.select(id)
    members = session_repository.members(session)
    all_members = member_repository.select_all()
    assignable_members = [x for x in filterfalse(lambda m: m.id in [member.id for member in members], all_members)]
    
    return render_template("sessions/show.html", session = session, members = members, assignable_members = assignable_members)