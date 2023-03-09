from flask_restx import Namespace, Resource, fields
# from flask_jwt_extended import jwt_required
from api.models.models import StudentModel

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
        return students
        

    @students_namespace.expect(student_model)
    @students_namespace.marshal_with(student_model)
    # @jwt_required
    def post(self):
        """Creates a new student"""
        student = StudentModel(**students_namespace.payload)
        # db.session.add(student)
        # db.session.commit()
        return student
