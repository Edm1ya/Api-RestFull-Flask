from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ResidentModel(db.Model):
    __tablename__ = 'resident'
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String,  nullable = False)
    phone = db.Column(db.BigInteger)
    email = db.Column(db.String, nullable= False)
    age = db.Column(db.Integer, nullable = False)
    address = db.Column(db.String, nullable = False)
    delivered_food = db.Column(db.Boolean, default=False, nullable=False)
    observation = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id, name=None, last_name = None, phone=None, email=None, age =None, address=None, delivered_food=None, observation=None ) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.age = age
        self.address = address
        self.delivered_food = delivered_food
        self.observation = observation


    def to_JSON(self):
        return{
            'id': self.id,
            'name':self.name,
            'last_name':self.last_name,
            'phone': self.phone,
            'email': self.email,
            'age': self.age,
            'address': self.address,
            'delivered_food': self.delivered_food,
            'observation': self.observation
        }