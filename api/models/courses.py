from ..utils import db
from enum import Enum

class TeachersName(Enum):
    Caleb = "Caleb Emeka"
    Olivia = "Olivia Nnemeso"
    Emeka = "Emeka Ebuka"
    Mercy = "Mervy Faleyimu"
    Iniobong = "Dr Iniobong Benson"

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    code = db.Column(db.String(128), nullable=False)
    grade = db.Column(db.String(128), nullable=False)
    teacher = db.Column(db.Enum(TeachersName), nullable=False)
    enrollment = db.relationship('Enrollment', backref='course')

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def __repr__(self):
        return f"<Course {self.id}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        