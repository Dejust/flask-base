"""
В модуле определен фабричный метод для создания инстанса приложения
"""
from flask import Flask
from flask_migrate import Migrate

from app.services.calculator import Calculator
from app.config import CommonConfig, get_config
from app.endpoints import pages
from app.models.common import DB


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
    if app.env_config.database_enabled:
        app.config['SQLALCHEMY_DATABASE_URI'] = app.env_config.DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        DB.init_app(app)
        DB.app = app
        app.db = DB

        # Init Migrations
        app.migrate = Migrate(app, app.db)

    # Add sample custom service
    app.calculator = Calculator(42)

    # Add endpoints
    _add_endpoints(app)

    return app


def get_application_for_env(env_name=None):
    """
    Возвращает application в окружении env_name
    Если env_name не указан, то будет окружение выбрано из переменной
    окружения $APP_ENV
    Если окружение не может быть определено, то выбрасывается AssertException
    :param env_name:
    """
    configuration = get_config(env_name)
    return get_application(configuration)


def get_test_application():
    """
    Возвращает application в тестовом окружении
    :return:
    """
    return get_application_for_env('test')
