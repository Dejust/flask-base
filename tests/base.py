import unittest

from app.factory import get_test_application


class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.test_app = get_test_application()
        self.test_client = self.test_app.test_client()

        self._set_up_database()

    def _set_up_database(self):
        db = self.test_app.db
        db.session.commit()
        db.drop_all()
        db.create_all()
