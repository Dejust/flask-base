"""
В модуле определен глобальный экземпляр Flask-приложения
"""

from app.config import get_config
from app.factory import get_application

app = get_application(get_config())
