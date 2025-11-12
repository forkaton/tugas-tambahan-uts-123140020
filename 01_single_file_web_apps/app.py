from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    """Fungsi view yang akan merespon request."""
    print('Incoming request')
    return Response('Hello World!')

if __name__ == '__main__':
    # Blok ini dieksekusi saat script dijalankan langsung
    with Configurator() as config:
        # 1. Menambahkan rute (URL)
        # Nama rute: 'hello', Pola URL: '/' (root)
        config.add_route('hello', '/')
        
        # 2. Menghubungkan rute ke view
        # Menghubungkan nama rute 'hello' ke fungsi 'hello_world'
        config.add_view(hello_world, route_name='hello')
        
        # 3. Membuat aplikasi WSGI dari konfigurasi
        app = config.make_wsgi_app()
        
    print("Server berjalan di http://0.0.0.0:6543")
    # 4. Menjalankan server
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()