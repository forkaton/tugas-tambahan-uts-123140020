import unittest
from pyramid import testing
from webtest import TestApp # <-- Impor TestApp dari webtest

class MyPackageFunctionalTests(unittest.TestCase):
    def setUp(self):
        """ Siapkan aplikasi WSGI untuk setiap tes """
        from mypackage import main # Impor 'main' factory dari __init__.py
        
        # Buat 'dummy' settings yang akan dibaca oleh app
        settings = {
            'app_greeting': 'Hello from .ini!',
        }
        
        # Buat aplikasi WSGI-nya
        app = main({}, **settings)
        
        # Bungkus aplikasi dengan WebTest.TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        """ Bersihkan setelah tes """
        del self.testapp
        testing.tearDown()

    def test_hello_world(self):
        """ Tes apakah rute '/' mengembalikan respons yang benar """
        
        # Simulasikan request GET ke URL '/'
        # 'status=200' berarti kita harap responsnya '200 OK'
        response = self.testapp.get('/', status=200)
        
        # Cek apakah body respons berisi teks yang kita harapkan
        # 'assertIn' mengecek apakah b'Hello from .ini!' ada di dalam response.body
        self.assertIn(b'Hello from .ini!', response.body)