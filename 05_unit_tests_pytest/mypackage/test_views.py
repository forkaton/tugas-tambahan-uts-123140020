import unittest
from pyramid import testing

class MyPackageViewsTests(unittest.TestCase):
    def test_hello_world(self):
        """Tes apakah view hello_world mengembalikan 'Hello from .ini!'"""
        from .views import hello_world
        
        # Buat request 'dummy' untuk testing
        request = testing.DummyRequest()
        
        # Set 'dummy' setting di registry
        request.registry.settings = {'app_greeting': 'Hello from .ini!'}
        
        # Panggil view function-nya langsung
        response = hello_world(request)
        
        # Cek apakah bodynya sesuai harapan
        self.assertEqual(response.body, b'Hello from .ini!')

