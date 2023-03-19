from flask import Flask
from flask_restx import Api
from .config.config import config_dict
from .students.views import students_namespace
from .auth.views import auth_namespace
from .utils import db
from .models.courses import Course
from .models.users import Student
from .models.enrollment import Enrollment
from flask_migrate import Migrate


def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)
    
    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)

    api.add_namespace(auth_namespace)
    api.add_namespace(students_namespace)

    # db.init_app(app)

    @app.context_processor
    def make_shell_context():
        return {
            'db': db,
            'Student': Student,
            'Course': Course,
            'Enrollment': Enrollment
        }
    
    return app
