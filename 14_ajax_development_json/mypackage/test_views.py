import unittest
from pyramid import testing
from webtest import TestApp 

class MyPackageFunctionalTests(unittest.TestCase):
    def setUp(self):
        # ... (setUp tetap sama) ...
        from mypackage import main 
        settings = { 'app_greeting': 'Hello from .ini!' }
        app = main({}, **settings)
        self.testapp = TestApp(app)

    def tearDown(self):
        # ... (tearDown tetap sama) ...
        del self.testapp
        testing.tearDown()

    def check_css_link(self, response):
        # ... (check_css_link tetap sama) ...
        link_tags = response.html.find_all('link', rel='stylesheet')
        self.assertTrue(len(link_tags) > 0, 'Tag <link> CSS tidak ditemukan')
        href = link_tags[0].get('href', '')
        self.assertIn('style.css', href, 'File "style.css" tidak ditemukan')

    def test_home_view(self):
        # ... (test_home_view tetap sama) ...
        response = self.testapp.get('/', status=200)
        self.assertIn(b'Nama dari query string: <strong>No Name</strong>', response.body)
        self.check_css_link(response) 

    def test_hello_view(self):
        # ... (test_hello_view tetap sama) ...
        response = self.testapp.get('/hello/Ansel', status=200)
        self.assertIn(b'Nama dari URL path: <strong>Ansel</strong>', response.body)
        self.check_css_link(response)

    def test_hello_json_view(self):
        """ Tes apakah endpoint JSON mengembalikan data yang benar. """
        print('Testing JSON endpoint...')
        
        # Panggil API endpoint kita
        response = self.testapp.get('/api/hello/Ansel', status=200)
        
        # WebTest punya helper .json untuk parsing JSON response
        response_data = response.json
        
        # Siapkan data yang kita harapkan
        expected_data = {
            'greeting': 'Hello from .ini!',
            'name': 'Ansel',
            'path': '/api/hello/Ansel'
        }
        
        # Bandingkan!
        self.assertEqual(response_data, expected_data)
        
        # Cek juga content-type header
        self.assertEqual(response.content_type, 'application/json')