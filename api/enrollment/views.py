from flask_restx import Namespace, Resource, fields
from flask import request
from ..models.courses import Course, TeachersName
from ..models.enrollment import Enrollment
from ..models.users import Student
from http import HTTPStatus
from ..utils import db
from flask_jwt_extended import jwt_required, get_jwt_identity

enrollment_namespace = Namespace('enrollment', description='name space for Order')

course_enrollment_model = enrollment_namespace.model(
    'Enrollment', {
        'student_id': fields.String(description='Name of course', required=True),
        'course_id': fields.String(description='Code of course', required=True),
        'grade': fields.Float(description='Size of order', required=True)
                }
)

enrollment_model = enrollment_namespace.model(
    'Course Enrollement', {
        'student_id': fields.String(description='Name of course', required=True),
        'course_id': fields.String(description='Code of course', required=True),
        'grade': fields.Float(description='Size of order', required=True)
    }
)

@enrollment_namespace.route('/courses')
class CourseGetCreate(Resource):
    @enrollment_namespace.marshal_with(enrollment_model)
    @enrollment_namespace.doc(
        description='Get all courses enrollment'
    )
    # @jwt_required()
    def get(self):
        """
            Get all orders
        """
        enrollment = Enrollment.query.all()

        return enrollment, HTTPStatus.OK

    @enrollment_namespace.expect(course_enrollment_model)
    @enrollment_namespace.marshal_with(enrollment_model)
    @enrollment_namespace.doc(
        description='Add a course'
    )
    # @jwt_required()
    def post(self):
        """
            Add a course
        """

        # username = get_jwt_identity()
        

        # current_user = Student.query.filter_by(username=username).first()

        data = request.get_json()

        new_enrollment = Enrollment(
            student_id = data.get('student_id'),
            course_id = data.get('course_id'),
            grade = data.get('grade')
        )

        # new_course.user = current_user

        new_enrollment.save()

        return new_enrollment, HTTPStatus.CREATED


# @enrollment_namespace.route('/order/<int:course_id>')
# class GetUpdateDelete(Resource):

#     @enrollment_namespace.marshal_with(course_model)
#     @enrollment_namespace.doc(
#         description='Retrieve an order by id',
#         params = {
#             'course_id': 'An ID for an order'
#         }
#     )
#     @jwt_required()
#     def get(self, course_id):
#         """
#             Retrieve an order by id
#         """
#         order = Course.query.get_or_404(course_id)

#         return order, HTTPStatus.OK

#     @enrollment_namespace.expect(course_model)
#     @enrollment_namespace.marshal_with(course_model)
#     @enrollment_namespace.doc(
#         description='Update an order by id',
#         params = {
#             'course_id': 'An ID for an order'
#         }
#     )
#     @jwt_required()
#     def put(self, course_id):
#         """
#             Update an order by id
#         """
#         course_to_update = Order.get_by_id(course_id)

#         data = enrollment_namespace.payload

#         course_to_update.quantity = data["quantity"]
#         course_to_update.size = data["size"]
#         course_to_update.flavour = data["flavour"]

#         db.session.commit()

#         return course_to_update, HTTPStatus.OK

#     @enrollment_namespace.doc(
#         description='Delete an order by id',
#         params = {
#             'course_id': 'An ID for an order'
#         }
#     )
#     @jwt_required()
#     def delete(self, course_id):
#         """
#             Delete an order by id
#         """

#         course_to_delete = Order.get_by_id(course_id)

#         course_to_delete.delete()

#         return {"message": "Deleted Successfully"}, HTTPStatus.OK
        


# @enrollment_namespace.route('/user/<int:user_id>/order/<int:course_id>')
# class GetSpecificOrderByUser(Resource):

#     @enrollment_namespace.marshal_with(course_model)
#     @enrollment_namespace.doc(
#         description='Get a user specific order by user id and order id',
#         params = {
#             'course_id': 'An ID for an order',
#             'user_id': 'An ID for a user'
#         }
#     )
#     @jwt_required()
#     def get(self, user_id, course_id):
#         """
#             Get a user specific order
#         """
#         user = User.get_by_id(user_id)

#         order = Order.query.filter_by(id=course_id).filter_by(user=user).first()

#         return order, HTTPStatus.OK

# @enrollment_namespace.route('/user/<int:user_id>/orders')
# class UserOrders(Resource):

#     @enrollment_namespace.marshal_list_with(course_model)
#     @enrollment_namespace.doc(
#         description='Get all user Orders by user id',
#         params = {
#             'user_id': 'An ID for a specific user\'s orders'
#         }
#     )
#     @jwt_required()
#     def get(self, user_id):
#         """
#             Get all user Order
#         """
#         user = User.get_by_id(user_id)

#         orders = user.orders

#         return orders, HTTPStatus.OK



# @enrollment_namespace.route('/order/status/<int:course_id>')
# class UpdateOrdersStatus(Resource):

#     @enrollment_namespace.expect(course_status_model)
#     @enrollment_namespace.marshal_with(course_model)
#     @enrollment_namespace.doc(
#         description='Update an order\'s Status',
#         params = {
#             'course_id': 'An ID for an order'
#         }
#     )
#     @jwt_required()
#     def patch(self, course_id):
#         """
#             Update an order's Status
#         """
#         data = enrollment_namespace.payload

#         course_to_update = Order.get_by_id(course_id)

#         course_to_update.course_status = data["course_status"]

#         db.session.commit()

#         return course_to_update, HTTPStatus.OK

