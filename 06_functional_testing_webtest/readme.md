# Analisis Percobaan 06: Functional Testing with WebTest

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari cara menulis *functional test*. Berbeda dengan *unit test* yang menguji fungsi terisolasi, *functional test* menguji seluruh alur kerja aplikasi (dari *routing* hingga *view*) tanpa perlu menjalankan server web sungguhan.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/test_views.py` di sini)
```python
import unittest
from pyramid import testing
from webtest import TestApp

class MyPackageFunctionalTests(unittest.TestCase):
    def setUp(self):
        """ Siapkan aplikasi WSGI untuk setiap tes """
        from mypackage import main
        settings = { 'app_greeting': 'Hello from .ini!' }
        app = main({}, **settings)
        self.testapp = TestApp(app)

    def tearDown(self):
        del self.testapp
        testing.config.Configurator().make_wsgi_app()

    def test_hello_world(self):
        """ Tes apakah rute '/' mengembalikan respons yang benar """
        response = self.testapp.get('/', status=200)
        self.assertIn(b'Hello from .ini!', response.body)
```

### 3. Hasil Percobaan (Screenshot)
<img width="956" height="1141" alt="Image" src="https://github.com/user-attachments/assets/27ffb3cd-f7d2-4e8c-b721-2147c5dd9d54" />

### 4. Analisis
* Konsep Utama: Functional Testing vs Unit Testing.

* Unit Test (Tutorial 05): Menguji fungsi hello_world sendirian. Kita harus membuat DummyRequest palsu dan mengisi registry secara manual.

* Functional Test (Tutorial 06): Menguji aplikasi secara keseluruhan. WebTest bertindak sebagai "browser palsu". Kita memanggil self.testapp.get('/') dan WebTest akan menangani routing, memanggil main, lalu memanggil view hello_world untuk kita.

* Cara Kerja:

  1. Fungsi setUp dijalankan sebelum setiap tes. Fungsi ini membuat instance aplikasi WSGI kita (menggunakan main factory) dan membungkusnya dengan TestApp.

  2. pytest menjalankan test_hello_world.

  3. self.testapp.get('/') membuat request GET palsu ke URL /.

  4. Aplikasi kita menerima request ini, sistem routing Pyramid mencocokkan / ke rute 'hello', dan memanggil view hello_world.

  5. View mengembalikan Response berisi "Hello from .ini!".

  6. self.assertIn(...) memeriksa bahwa body dari Response itu memang berisi teks yang kita harapkan. Jika ya, tes LULUS.

* Masalah/Error: Tidak ada error atau masalah.

### 5. Kesimpulan
Functional test memberikan keyakinan lebih tinggi bahwa komponen-komponen aplikasi (seperti routing dan view) bekerja sama dengan benar. WebTest sangat berguna karena memungkinkan kita menguji alur HTTP secara lengkap tanpa perlu repot menjalankan server.