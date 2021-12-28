from django.test import SimpleTestCase

# Create your tests here.
# SimpleTestCase is for when you do not have a database, TestCase is for when you do have a database.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
        # The status code for a successful HTTP request is 200
    
    def test_about_page_status_code(self):
        response=self.client.get('/about')
        self.assertEqual(response.status_code,200)
