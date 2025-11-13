import unittest
from pyramid import testing
from webtest import TestApp 
# Impor HTTPFound untuk mengecek redirect
from pyramid.httpexceptions import HTTPFound 

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
        self.check_css_link(response) 

    def test_hello_view(self):
        # ... (test_hello_view tetap sama) ...
        response = self.testapp.get('/hello/Ansel', status=200)
        self.check_css_link(response)

    def test_hello_json_view(self):
        # ... (test_hello_json_view tetap sama) ...
        response = self.testapp.get('/api/hello/Ansel', status=200)
        self.assertEqual(response.content_type, 'application/json')
   
    def test_edit_view_get(self):
        """ Tes apakah GET ke /edit menampilkan form. """
        print('Testing GET /hello/Ansel/edit...')
        response = self.testapp.get('/hello/Ansel/edit', status=200)
        
        # Cek apakah form-nya ada di HTML
        self.assertIn(b'<form method="post">', response.body)
        self.assertIn(b'New Greeting:', response.body)

    def test_edit_view_post(self):
        """ Tes apakah POST ke /edit memproses data dan redirect. """
        print('Testing POST /hello/Ansel/edit...')
        
        # Kirim data form 'new_greeting'='New Hi'
        response = self.testapp.post(
            '/hello/Ansel/edit', 
            {'new_greeting': 'New Hi'},
            status=302 # <-- Harapkan redirect (302 Found)
        )
        
        # Pastikan kita di-redirect ke URL yang benar
        self.assertEqual(response.location, 'http://localhost/hello/Ansel')
        
        response_redirected = response.follow()
        self.assertIn(b'<h1>New Hi</h1>', response_redirected.body)