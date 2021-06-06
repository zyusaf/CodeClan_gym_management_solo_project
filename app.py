from flask import Flask, render_template

# from controllers.member_sessions_controller import member_sessions_blueprint
# from controllers.sessions_controller import sessions_blueprint
from controllers.member_controller import members_blueprint

app = Flask(__name__)

# app.register_blueprint(member_sessions_blueprint)
# app.register_blueprint(sessions_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)