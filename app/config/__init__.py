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
    DATABASE_URI = os.getenv('DATABASE_URI')

    @property
    def is_debug(self):
        return self.DEBUG

    @classmethod
    @property
    def ENV_NAME(cls):
        raise NotImplementedError


class DevConfig(CommonConfig):
    """Конфигурация приложения для разработки на локальных машинах разработчиков"""

    @property
    def ENV_NAME(self):
        return 'dev'

    DEBUG = True


class TestConfig(CommonConfig):
    """Конфигурация приложения для запуска автоматических тестов"""

    @property
    def ENV_NAME(self):
        return 'test'

    DEBUG = True


class StagingConfig(CommonConfig):
    """Конфигурация приложения для запуска пре-продакшна"""

    @property
    def ENV_NAME(self):
        return 'staging'


class ProductionConfig(CommonConfig):
    """Конфигурация приложения для запуска продакшна"""

    @property
    def ENV_NAME(self):
        return 'production'


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
    :rtype: CommonConfig
    """
    if app_env_name is None:
        app_env_name = os.getenv('APP_ENV')

    assert app_env_name in _ENABLED_CONFIGURATIONS, \
        'Invalid env name: {}. Enabled environments: {}'.format(app_env_name, ", ".join(_ENABLED_CONFIGURATIONS.keys()))

    return _ENABLED_CONFIGURATIONS[app_env_name]
