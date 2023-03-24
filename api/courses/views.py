from flask_restx import Namespace, Resource, fields
from flask import request
from ..models.courses import Course, TeachersName
from ..models.users import Student
from http import HTTPStatus
from ..utils import db
from flask_jwt_extended import jwt_required, get_jwt_identity

course_namespace = Namespace('course', description='name space for Order')

course_model = course_namespace.model(
    'Course', {
        'id': fields.Integer(description='An ID'),
        'name': fields.String(description='Name of course', required=True),
        'code': fields.String(description='Code of course', required=True),
        'grade': fields.String(description='Grade of course', required=True),
        'teacher': fields.String(description='Size of order', required=True,
            enum = ['Iniobong Benson', 'Oluwaseun Oluwafemi', 'Eno-obong Ella', 'Mercy Faleyimu']
            )
                }
)

course_add_model = course_namespace.model(
    'Course', {
        
        'name': fields.String(description='Name of course', required=True),
        'code': fields.String(description='Code of course', required=True),
        'teacher': fields.String(description='Size of order', required=True),
    }
)

@course_namespace.route('/courses')
class CourseGetCreate(Resource):

    @course_namespace.marshal_list_with(course_model)
    @course_namespace.doc(
        description='Get all courses'
    )
    # @jwt_required()
    def get(self):
        """
            Get all orders
        """
        courses = Course.query.all()

        return courses, HTTPStatus.OK

    @course_namespace.expect(course_model)
    @course_namespace.marshal_with(course_model)
    @course_namespace.doc(
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

        new_course = Course(
            name = data['name'],
            code = data['code'],
            grade = data['grade'],
            teacher = data['teacher']
        )

        # new_course.user = current_user

        new_course.save()

        return new_course, HTTPStatus.CREATED


@course_namespace.route('/order/<int:course_id>')
class GetUpdateDelete(Resource):

    @course_namespace.marshal_with(course_model)
    @course_namespace.doc(
        description='Retrieve an order by id',
        params = {
            'course_id': 'An ID for an order'
        }
    )
    @jwt_required()
    def get(self, course_id):
        """
            Retrieve an order by id
        """
        order = Course.query.get_or_404(course_id)

        return order, HTTPStatus.OK

#     @course_namespace.expect(course_model)
#     @course_namespace.marshal_with(course_model)
#     @course_namespace.doc(
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

#         data = course_namespace.payload

#         course_to_update.quantity = data["quantity"]
#         course_to_update.size = data["size"]
#         course_to_update.flavour = data["flavour"]

#         db.session.commit()

#         return course_to_update, HTTPStatus.OK

#     @course_namespace.doc(
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
        


# @course_namespace.route('/user/<int:user_id>/order/<int:course_id>')
# class GetSpecificOrderByUser(Resource):

#     @course_namespace.marshal_with(course_model)
#     @course_namespace.doc(
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

# @course_namespace.route('/user/<int:user_id>/orders')
# class UserOrders(Resource):

#     @course_namespace.marshal_list_with(course_model)
#     @course_namespace.doc(
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



# @course_namespace.route('/order/status/<int:course_id>')
# class UpdateOrdersStatus(Resource):

#     @course_namespace.expect(course_status_model)
#     @course_namespace.marshal_with(course_model)
#     @course_namespace.doc(
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
#         data = course_namespace.payload

#         course_to_update = Order.get_by_id(course_id)

#         course_to_update.course_status = data["course_status"]

#         db.session.commit()

#         return course_to_update, HTTPStatus.OK

