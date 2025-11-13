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
        # --- Tes 1: Tanpa query parameter ---
        response = self.testapp.get('/', status=200)
        
        # Cek h1 (masih sama)
        h1_tag = response.html.find('h1')
        self.assertEqual(h1_tag.text.strip(), 'Hello from .ini!')
        
        # Cek <p> untuk nama (harus default 'No Name')
        # response.text berisi teks HTML
        self.assertIn(b'Nama dari query string: <strong>No Name</strong>', response.body)
        
        # Cek <p> untuk path (harus '/')
        self.assertIn(b'Path URL saat ini: <strong>/</strong>', response.body)

        # --- Tes 2: DENGAN query parameter ---
        response = self.testapp.get('/?name=Ansel', status=200)
        
        # Cek <p> untuk nama (harus 'Ansel')
        self.assertIn(b'Nama dari query string: <strong>Ansel</strong>', response.body)