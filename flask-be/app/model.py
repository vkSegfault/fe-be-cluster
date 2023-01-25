from app_setup import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    money = db.Column(db.Integer())

    def __init__(self, name, money) -> None:
        super().__init__()
        self.name = name
        self.money = money

    def __repr__(self) -> str:
        return f'ID: {self.id}'

    def read_all():
        pass

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, name, money):
        self.name = name
        self.money = money