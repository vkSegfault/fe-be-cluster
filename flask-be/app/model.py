from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
from .app_controller import bcrypt
from .app_controller import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __table_args__ = ( db.UniqueConstraint('name'),)

    # all self.name is mapped to name here
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=200), unique=True, nullable=False)   # table must be created with `unique=True` constraint to actually block any dups (creating table without it first will not work)
    password_hash = db.Column(db.String(length=60), nullable=False)
    money = db.Column(db.Integer(), default=0)
    note = db.relationship('Note', backref='ownee', lazy=True)   # user owns a note

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def verify_password(self, provided_password):
        isCorrectPassword = bcrypt.check_password_hash(self.password_hash, provided_password)
        if isCorrectPassword:
            return True

    def __init__(self, name: str, password: str , money: int) -> None:
        super().__init__()
        self.name = name
        self.password = password
        self.money = money

    # def __init__(self) -> None:
    #     super().__init__()

    def __repr__(self) -> str:
        return f'ID: {self.id}'

    def read_all(self):
        all = self.query.all()
        return all

    def read_one(self, name):
        one = self.query.filter_by(name=name).first()   # name is unique so it will be always one, for many we need to iterate over, also name returns a string object - without it 
        return one

    def add(self):
        # if db.session.query(self).filter(name='Janusz').exists():
        #     print('Janusz exists')
        #     return
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, name, money):
        self.name = name
        self.money = money
        user = self.query.get(name)
        print(user)
        db.session.commit()   # is this enough to update ?

    def exist(self, name: str):
        user = self.query.filter_by(name=name).first()
        if user:   # if there is not user in DB None will be returned
            print( user )
            return user


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer(), primary_key=True)
    note = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))