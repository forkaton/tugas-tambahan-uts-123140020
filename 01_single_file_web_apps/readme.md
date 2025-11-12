# Analisis Percobaan 01: Single-File Web Applications

### 1. Tujuan Percobaan
Tujuan dari percobaan ini adalah untuk memahami cara membuat aplikasi web Pyramid yang paling sederhana hanya dengan menggunakan satu file Python dan menjalankannya dengan server WSGI bawaan Python.

### 2. Kode Program Utama
```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello World!')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
```
 
### 3. Hasil Percobaan (Screenshot)

<img width="1878" height="1093" alt="Image" src="https://github.com/user-attachments/assets/1bca5557-9ab3-4fe2-91c4-d48f2bcdc222" />

### 4. Analisis
* Konsep Utama: Konsep yang dipelajari adalah "view callable" (fungsi hello_world) yang dihubungkan ke sebuah URL (/) melalui sistem routing.

* Cara Kerja:

  1. Configurator digunakan untuk mengatur aplikasi.
  2. config.add_route('hello', '/') mendaftarkan bahwa URL / akan memiliki nama rute 'hello'.
  3. config.add_view(hello_world, route_name='hello') memberitahu Pyramid: "Jika ada yang mengakses rute 'hello', jalankan fungsi hello_world".
  4. make_wsgi_app() membuat aplikasi WSGI yang bisa dimengerti oleh server.
  5. make_server dari wsgiref (bawaan Python) digunakan untuk menjalankan aplikasi di port 6543.

* Masalah/Error: Tidak ada masalah. Program berjalan lancar.

### 5. Kesimpulan
Percobaan ini menunjukkan bahwa Pyramid sangat minimalis dan fleksibel. Kita bisa membuat aplikasi web yang valid hanya dalam satu file tanpa perlu struktur folder yang rumit.