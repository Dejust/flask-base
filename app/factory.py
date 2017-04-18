"""
В модуле определен фабричный метод для создания инстанса приложения
"""
from flask import Flask
from flask_migrate import Migrate

from app.config import CommonConfig, get_config
from app.endpoints import pages
from app.models.common import db


def _add_endpoints(app: Flask):
    app.add_url_rule('/', 'pages.index', pages.index_page, methods=['GET'])


def get_application(configuration: CommonConfig):
    """
    Возвращает инстанс Flask-приоложения для соответствующего окружения
    :param configuration: конфиуграция
    """
    app = Flask(__name__)
    app.env_config = configuration

    # Init SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = app.env_config.DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    db.app = app
    app.db = db

    # Init Migrations
    app.migrate = Migrate(app, app.db)

    # Add endpoints
    _add_endpoints(app)

    return app


def get_application_for_env(env_name=None):
    configuration = get_config(env_name)
    return get_application(configuration)


def get_test_application():
    return get_application_for_env('test')
