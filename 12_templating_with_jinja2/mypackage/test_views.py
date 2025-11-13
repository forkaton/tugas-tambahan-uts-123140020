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

    def test_home_view(self): 
        # --- Tes 1: Tanpa query parameter (ke root) ---
        response = self.testapp.get('/', status=200)
        self.assertIn(b'Nama dari query string: <strong>No Name</strong>', response.body)
        
        # --- Tes 2: DENGAN query parameter (ke root) ---
        response = self.testapp.get('/?name=Ansel', status=200)
        self.assertIn(b'Nama dari query string: <strong>Ansel</strong>', response.body)

    def test_hello_view(self): # <-- TAMBAH TES BARU
        # --- Tes 3: Dengan URL path dinamis ---
        response = self.testapp.get('/hello/Ansel', status=200)
        
        # Cek apakah dia pakai template hello.pt yang benar
        self.assertIn(b'Nama dari URL path: <strong>Ansel</strong>', response.body)