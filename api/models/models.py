from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StudentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    teacher = db.Column(db.String(128), nullable=False)
    students = db.relationship('Enrollment', back_populates='course')

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    grade = db.Column(db.Float)
    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='students')

    @property
    def gpa(self):
        if self.grade is None:
            return None
        elif self.grade >= 3.7:
            return 4.0
        elif self.grade >= 3.3:
            return 3.7
        elif self.grade >= 3.0:
            return 3.3
        elif self.grade >= 2.7:
            return 3.0
        elif self.grade >= 2.3:
            return 2.7
        elif self.grade >= 2.0:
            return 2.3
        elif self.grade >= 1.7:
            return 2.0
        elif self.grade >= 1.3:
            return 1.7
        elif self.grade >= 1.0:
            return 1.3
        else:
            return 0.0

StudentModel.enrollments = db.relationship('Enrollment', back_populates='student')
