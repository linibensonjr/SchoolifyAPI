from ..utils import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    course = db.relationship('Enrollment', backref='student')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Student {self.id}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


