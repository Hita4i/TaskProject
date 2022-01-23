import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


'''$env:FLASK_APP="base.py" '''

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jn5wpthp9gdsfn432lnnvsd'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{ROOT_DIR}/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.email}'
