from flask_restx import Namespace, Resource, fields
# from flask_jwt_extended import jwt_required
from api.models.models import StudentModel
from http import HTTPStatus

students_namespace = Namespace('students', description='namespace for students')



student_model = students_namespace.model('Student', {
    'id': fields.Integer(),
    'name': fields.String(),
    'email': fields.String()
})

@students_namespace.route('/')
class StudentList(Resource):
    # @ns.marshal_list_with(student_model)
    # @jwt_required
    def get(self):
        """Returns a list of all students"""
        students = StudentModel.query.all()
        if students:
            return students, HTTPStatus.OK
        else:
            return HTTPStatus.BAD_REQUEST
        

    @students_namespace.expect(student_model)
    @students_namespace.marshal_with(student_model)
    # @jwt_required
    def post(self):
        """Creates a new student"""
        student = StudentModel(**students_namespace.payload)
        # db.session.add(student)
        # db.session.commit()
        return student
    
@students_namespace.route('student/<int:id>')
class StudentUpdateDelete(Resource):
    def get(self, student_id):
        '''Get a single order'''
        student = StudentModel.query.filter_by(student_id)
        return {"message": "Hello get order by id here"}

    def patch(self, student_id):
        '''Update an order'''

        student_to_update = StudentModel.query.get_by_id(student_id)
        try:
            data = request.get_json()

            student_to_update.name = data.get('name')

        except Exception as e:
            return {"message": "Hello update order by id here"}

    def delete(self, order_id):
        '''Delete an order'''
        return {"message": "Hello delete order by id here"}
