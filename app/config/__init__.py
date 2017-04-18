"""
В модуле определены конфигурации приложения для различных окружений
Список доступных окружений перечислены в _AVAILABLE_ENVIRONMENTS
"""

import os


class CommonConfig:
    """Общие настройики приложения"""

    # Общие параметры
    DEBUG = False

    # Параметры базы данных
    DATABASE_URI = os.getenv('DATABASE_URI', None)

    ENV_NAME = None

    @property
    def is_debug(self):
        return self.DEBUG

    @property
    def database_enabled(self):
        return self.DATABASE_URI is not None


class DevConfig(CommonConfig):
    """Конфигурация приложения для разработки на локальных машинах разработчиков"""

    ENV_NAME = 'dev'

    DEBUG = True


class TestConfig(CommonConfig):
    """Конфигурация приложения для запуска автоматических тестов"""

    ENV_NAME = 'test'

    DEBUG = True


class StagingConfig(CommonConfig):
    """Конфигурация приложения для запуска пре-продакшна"""

    ENV_NAME = 'staging'


class ProductionConfig(CommonConfig):
    """Конфигурация приложения для запуска продакшна"""

    ENV_NAME = 'production'


_AVAILABLE_CONFIGURATIONS = [
    ProductionConfig,
    StagingConfig,
    TestConfig,
    DevConfig
]

_ENABLED_CONFIGURATIONS = {c.ENV_NAME: c for c in map(lambda x: x(), _AVAILABLE_CONFIGURATIONS)}


def get_config(app_env_name=None):
    """
    Метод возвращает конфигурацию приложения для задананного окружения
    Если окружение не задано, то будет использовано значение из переменной окружений %APP_ENV%
    :param app_env_name:
    :rtype: CommonConfig
    """
    if app_env_name is None:
        app_env_name = os.getenv('APP_ENV')

    assert app_env_name in _ENABLED_CONFIGURATIONS, \
        'Invalid $APP_ENV name: {}. Enabled environments: {}'.format(app_env_name, ", ".join(_ENABLED_CONFIGURATIONS.keys()))

    return _ENABLED_CONFIGURATIONS[app_env_name]
