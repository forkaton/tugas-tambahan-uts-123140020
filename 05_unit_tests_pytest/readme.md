# Analisis Percobaan 05: Unit Tests and pytest

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari cara menulis dan menjalankan *unit test* untuk *view* Pyramid. Kita menggunakan *library* `pytest` dan `pyramid.testing` untuk menguji logika *view* secara terisolasi.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/tests.py` di sini)
```python
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
```

### 3. Hasil Percobaan (Screenshot)
<img width="959" height="1138" alt="Image" src="https://github.com/user-attachments/assets/6af4535d-6c47-45ce-b5ed-a98104301edd" />

### 4. Analisis
* Konsep Utama: Unit Testing. Kita tidak menguji seluruh aplikasi web, tapi hanya satu unit kecil (fungsi hello_world) untuk memastikan logikanya benar.

* Cara Kerja:

  1. pytest akan secara otomatis mencari file yang diawali test_ atau diakhiri _test.py, dan menjalankan fungsi yang diawali test_.

  2. pyramid.testing.DummyRequest() membuat objek request palsu (dummy) yang cukup untuk menguji view kita.

  3. Kita "mengisi" registry palsu (request.registry.settings) dengan data yang kita harapkan (greeting message).

  4. Kita memanggil fungsi hello_world langsung, seperti fungsi Python biasa.

  5. self.assertEqual(response.body, b'Hello from .ini!') adalah assertion. Ini adalah inti dari tes: "Saya harap response body-nya adalah 'Hello from .ini!'". Jika benar, tes LULUS (PASS). Jika salah, tes GAGAL (FAIL).

  6. Huruf b di depan ( b'Hello...' ) berarti bytes, karena response body di-encode sebagai bytes, bukan string biasa.

* Masalah/Error: Tidak ada masalah, program berjalan dengan baik.

### 5. Kesimpulan
Unit test sangat penting untuk memastikan setiap bagian kecil dari kode kita bekerja dengan benar. Ini membantu kita menemukan bug lebih awal, terutama saat aplikasi semakin kompleks, tanpa harus menjalankan server dan mengklik-klik di browser secara manual.