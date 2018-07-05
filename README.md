# flaskwp
Backend for wordpress database in python flask

## Installation
```
pip install flask-wp
```

## Basic Usage
```python
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

if __name__ == "__main__":
    app.run(debug=True)
```

## To follow MVC pattern
create a models.py file 
```python
__all__ = (
	"User"
)

# add a method to WPUser class
def get_email(user):
    return user.user_email
fwp.User.get_email = get_email

User = fwp.User
```
