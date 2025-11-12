# Analisis Percobaan 02: Python Packages for Pyramid Applications

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mengubah aplikasi dari satu file menjadi sebuah *Python package* yang dapat di-install. Ini memperkenalkan cara standar untuk mengelola proyek Pyramid dan cara baru untuk menjalankan server menggunakan `pserve`.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/__init__.py` di sini sebagai contoh)
```python
from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        config.add_route('hello', '/')
        config.add_view('mypackage.views.hello_world', route_name='hello')
        return config.make_wsgi_app()
```

### 3. Hasil Percobaan (Screenshot)
<img width="1865" height="1084" alt="Image" src="https://github.com/user-attachments/assets/1de7f2a6-2390-44be-9d99-1e1030d7c6c8" />

### 4. Analisis
* Konsep Utama: Konsep utamanya adalah packaging dan entry points.

setup.py: Mendefinisikan proyek kita sebagai package yang bisa di-install (mypackage).

development.ini: File konfigurasi untuk server. Bagian [app:main] menunjuk ke entry point yang didefinisikan di setup.py. Bagian [server:main] memberitahu pserve untuk menggunakan waitress di port 6543.

pserve: Perintah baru untuk menjalankan server. Dia membaca file .ini untuk tahu apa yang harus dijalankan. Ini lebih baik daripada python app.py karena memisahkan konfigurasi dari kode.

* Cara Kerja:

  1. Kita menjalankan pserve development.ini.

  2. pserve membaca development.ini dan melihat bahwa dia harus menggunakan waitress sebagai server ([server:main]).

  3. Dia juga melihat bahwa aplikasi utamanya ([app:main]) adalah egg:mypackage#main.

  4. Ini memicu entry point di setup.py, yang menunjuk ke fungsi main di mypackage/__init__.py.

  5. Fungsi main dieksekusi, mengatur rute (/) dan menghubungkannya ke view (mypackage.views.hello_world).

  6. Aplikasi WSGI dibuat dan diserahkan ke server waitress.

* Masalah/Error: (Tulis "Tidak ada masalah." jika lancar)

### 5. Kesimpulan
Dengan mengubah aplikasi menjadi package, kita membuat struktur proyek yang lebih rapi, terorganisir, dan siap untuk dikembangkan lebih lanjut. Logika aplikasi (views) terpisah dari konfigurasi (routes) dan pengaturan server (.ini).