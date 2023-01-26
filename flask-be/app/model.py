from .app import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __table_args__ = ( db.UniqueConstraint('name'),)

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)   # table must be created with `unique=True` constraint to actually block any dups (creating table without it first will not work)
    money = db.Column(db.Integer())
    note = db.relationship('Note')

    def __init__(self, name: str, money: int) -> None:
        super().__init__()
        self.name = name
        self.money = money

    def __repr__(self) -> str:
        return f'ID: {self.id}'

    def read_all():
        pass

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


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer(), primary_key=True)
    note = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))