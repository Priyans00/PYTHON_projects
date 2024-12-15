from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Truth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Truth {self.question}>'
    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'created_at': self.created_at
        }
    

class Dare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    challenge = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Dare {self.challenge}>'
    def to_dict(self):
        return {
            'id': self.id,
            'challenge': self.challenge,
            'created_at': self.created_at
        }