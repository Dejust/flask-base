"""
В модуле определен глобальный экземпляр Flask-приложения
"""
from app.factory import get_application_for_env

app = get_application_for_env()
