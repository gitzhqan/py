#encoding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
   SQLALCHEMY_COMMIT_TEARDOWN = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120),unique=True)

    def __init__(self, username,email):
        self.username = username
        self.email =email

    def _repr_(self):
        return '<User %r>' % self.username