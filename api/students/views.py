from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from ..models.users import Student
from ..utils import db
from http import HTTPStatus

students_namespace = Namespace('students', description='namespace for students')

student_model = students_namespace.model(
    'Student', {
    'id': fields.Integer(readonly=True, description='The unique identifier of a user'),
    'name': fields.String(),
    'email': fields.String(),
    'course' : fields.String(),
    'date_created': fields.DateTime(),
    'date_modified': fields.DateTime()
})

@students_namespace.route('/')
class StudentList(Resource):
    @students_namespace.marshal_with(student_model)
    @jwt_required
    def get(self):
        """Returns a list of all students"""
        students = Student.query.all()
        return students, HTTPStatus.OK

    @students_namespace.expect(student_model)
    @students_namespace.marshal_with(student_model)
    @jwt_required
    def post(self):
        """Creates a new student"""
        student = Student(**students_namespace.payload)
        db.session.add(student)
        db.session.commit()
        return student
    
@students_namespace.route('/student/<int:student_id>')
class StudentUpdateDelete(Resource):
    @students_namespace.marshal_with(student_model)
    def get(self, student_id):
        '''Get a single student'''
        student = Student.query.get_or_404(student_id)
        if student:
            return student, HTTPStatus.OK
        
        return HTTPStatus.BAD_REQUEST
    
    @students_namespace.expect(student_model)
    @students_namespace.marshal_with(student_model)
    def patch(self, student_id):
        '''Update an student'''

        student_to_update = Student.query.get_or_404(student_id)
        if student_to_update:
            try:
                data = request.get_json()

                student_to_update.name = data.get('name')
                student_to_update.course = data.get('course')

            except Exception as e:
                return {"message": "Hello update student by id here"}
        
        return {"message": "Hello update student by id here"}, HTTPStatus.OK

    def delete(self, student_id):
        '''Delete an student'''

        student_to_update = Student.query.get_or_404(student_id)
        if student_to_update:
            student_to_update.delete()
        
            return {"message": "Student successfully deleted"}, HTTPStatus.OK
        else:
    
         return {"message": "Student not found"}, HTTPStatus.BAD_REQUEST
