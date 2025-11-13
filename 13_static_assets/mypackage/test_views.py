import unittest
from pyramid import testing
from webtest import TestApp 

class MyPackageFunctionalTests(unittest.TestCase):
    def setUp(self):
        from mypackage import main 
        settings = { 'app_greeting': 'Hello from .ini!' }
        app = main({}, **settings)
        self.testapp = TestApp(app)

    def tearDown(self):
        del self.testapp
        testing.tearDown()

    def check_css_link(self, response):
        """ 
        Helper untuk mengecek link CSS di response.
        Ini versi yang lebih pintar (robust).
        """
        # response.html adalah fitur dari WebTest untuk parsing HTML
        # Kita cari SEMUA link stylesheet
        link_tags = response.html.find_all('link', rel='stylesheet')
        
        # Pastikan setidaknya ada satu link
        self.assertTrue(
            len(link_tags) > 0, 
            'Tag <link rel="stylesheet"> tidak ditemukan'
        )
        
        # Ambil href dari link pertama dan cek
        href = link_tags[0].get('href', '')
        self.assertIn(
            'style.css', 
            href, 
            'File "style.css" tidak ditemukan di dalam href link tag'
        )

    def test_home_view(self):
        response = self.testapp.get('/', status=200)
        self.assertIn(b'Nama dari query string: <strong>No Name</strong>', response.body)
        self.check_css_link(response) 

    def test_hello_view(self):
        response = self.testapp.get('/hello/Ansel', status=200)
        self.assertIn(b'Nama dari URL path: <strong>Ansel</strong>', response.body)
        self.check_css_link(response) 