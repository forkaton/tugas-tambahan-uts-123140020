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

    def test_hello_world(self):
        response = self.testapp.get('/', status=200)
        
        # Dulu: self.assertIn(b'Hello from .ini!', response.body)
        # Sekarang: kita cek apakah ada <h1>Hello from .ini!</h1> di body
        # Kita hapus spasi dengan .strip() agar lebih robust
        expected_text = b'<h1>Hello from .ini!</h1>'
        
        # response.html adalah fitur dari WebTest untuk parsing HTML
        h1_tag = response.html.find('h1')
        self.assertIsNotNone(h1_tag) # Pastikan tag h1' ada
        self.assertEqual(h1_tag.text.strip(), 'Hello from .ini!')