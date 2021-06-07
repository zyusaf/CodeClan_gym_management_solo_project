from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member_session import Member_Session
import repositories.member_session_repository as member_session_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

member_sessions_blueprint = Blueprint("member_sessions", __name__)

@member_sessions_blueprint.route("/member_sessions")
def member_sessions():
    member_sessions = member_session_repository.select_all()
    return render_template("member_sessions/index.html", member_sessions = member_sessions)

@member_sessions_blueprint.route("/member_sessions/new", methods=['GET'])
def new_member_session():
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("member_sessions/new.html", members = members, sessions = sessions)

@member_sessions_blueprint.route("/member_sessions", methods=['POST'])
def create_member_session():
    member_id = request.form['member_id']
    session_id = request.form['session_id']
    review = request.form['review']
    member = member_repository.select(member_id)
    session = session_repository.select(session_id)
    member_session = Member_Session(member, session, review)
    member_session_repository.save(member_session)
    return redirect('/member_sessions')

@member_sessions_blueprint.route("/member_sessions/<id>/delete", methods=['POST'])
def delete_member_session(id):
    member_session_repository.delete(id)
    return redirect('/member_sessions')
