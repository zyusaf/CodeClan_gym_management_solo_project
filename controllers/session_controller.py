from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository

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