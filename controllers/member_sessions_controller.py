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


