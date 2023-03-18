from ..utils import db

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    grade = db.Column(db.Float)
    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='students')

    def __repr__(self):
        return f"<Enrollment {self.id}>"
    
    def __init__(self, student_id, course_id, grade):
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Enrollment.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Enrollment.query.get(id)
    