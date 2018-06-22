from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wp import FlaskWP

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {
    'wordpress': 'mysql+pymysql://modopiausr:123@localhost/modopiadb'
}
db = SQLAlchemy(app)
wp = FlaskWP(db, app)

@app.route('/')
def index():
    post = wp.Post.query.first()
    print(post)
    return "hellow"


app.run(debug=True)