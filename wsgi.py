import flask
from flask import Flask
from flask_wp import FlaskWP
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {
    "wordpress" : "mysql+pymysql://modopiausr:123@localhost/modopiadb"
}
db = SQLAlchemy(app)
fwp = FlaskWP(db, app)

@app.route("/")
def index():
    return flask.jsonify([{'user_email': usr.user_email} for usr in fwp.User.query.all()])

app.run(debug=True)
