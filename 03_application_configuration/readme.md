# Analisis Percobaan 03: Application Configuration with .ini Files

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari cara membaca nilai konfigurasi *custom* (buatan sendiri) dari file `.ini` ke dalam logika aplikasi Python.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/__init__.py` di sini)
```python
from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        # Baca setting 'app_greeting' dari file .ini
        greeting = settings.get('app_greeting', 'Hello World!')
        
        # Simpan nilai greeting ke registry config
        config.registry.settings['app_greeting'] = greeting

        config.add_route('hello', '/')
        config.add_view('mypackage.views.hello_world', route_name='hello')
        return config.make_wsgi_app()
```

### 3. Hasil Percobaan (Screenshot)
<img width="1865" height="1089" alt="Image" src="https://github.com/user-attachments/assets/05250464-9899-4133-8a89-73ddc9ce7341" />

### 4. Analisis
* Konsep Utama: Memisahkan konfigurasi dari kode File .ini adalah tempat untuk menyimpan "data" (seperti greeting message, database URL, API key), dan kode Python kita membacanya.

* Cara Kerja:

  1. Saat pserve dijalankan, ia memuat semua pengaturan di [app:main] (termasuk app_greeting) ke dalam kamus (dictionary) settings.

  2. Kamus settings ini diteruskan ke fungsi main di __init__.py.

  3. Di dalam main, kita mengambil nilai app_greeting dari settings menggunakan settings.get(...).

  4. Nilai ini kemudian kita simpan di config.registry.settings agar bisa diakses secara global oleh bagian lain dari aplikasi.

  5. Fungsi view (hello_world) kemudian mengambil nilai tersebut dari registry menggunakan request.registry.settings['app_greeting'] dan menampilkannya sebagai Response.

* Masalah/Error: (Tulis "Tidak ada masalah." jika lancar)

### 5. Kesimpulan
Menggunakan file .ini untuk konfigurasi membuat aplikasi lebih fleksibel. Kita bisa mengubah pesan sapaan (atau koneksi database) tanpa harus mengubah kode Python, cukup ubah file .ini dan restart server.