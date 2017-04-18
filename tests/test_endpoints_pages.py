from tests.base import IntegrationTestCase
from flask import url_for


class TestIndexPage(IntegrationTestCase):
    def test_that_index_page_available(self):
        with self.test_app.test_request_context():
            response = self.test_client.get(url_for('pages.index'))
            self.assertEqual(200, response.status_code)
