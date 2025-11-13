# Analisis Percobaan 07: Basic Web Handling With Views

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari cara alternatif mendaftarkan *view* menggunakan *decorator* `@view_config` dan `config.scan()`, yang memisahkan konfigurasi *view* dari file `__init__.py`.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/views.py` di sini)
```python
from pyramid.response import Response
from pyramid.view import view_config # <-- Impor

# @view_config memberi tahu Pyramid bahwa ini adalah view
# 'route_name='hello'' menghubungkannya ke rute 'hello'
@view_config(route_name='hello') # <-- Dekorator
def hello_world(request):
    # Ambil nilai 'app_greeting' dari registry
    greeting = request.registry.settings['app_greeting']
    
    print('Incoming request, greeting is:', greeting)
    return Response(greeting)
```

### 3. Hasil Percobaan (Screenshot)
<img width="955" height="1139" alt="Image" src="https://github.com/user-attachments/assets/72e78cd1-33cc-41f7-94c5-6748d9280eb1" />

### 4. Analisis
* Konsep Utama: Decorator dan Scanning.

* @view_config: Ini adalah "label" atau decorator yang kita tempelkan di atas sebuah fungsi. Label ini berisi metadata (data tentang data) yang memberitahu Pyramid, "Hei, fungsi ini adalah view untuk rute bernama 'hello'".

* config.scan('.views'): Perintah ini, yang kita letakkan di __init__.py, memberitahu Pyramid saat startup, "Tolong periksa file .views (dan file lain di package), cari semua fungsi yang punya label @view_config, dan daftarkan mereka secara otomatis."

* Cara Kerja:

  1. Saat pserve dijalankan, fungsi main di __init__.py dieksekusi.

  2. config.scan('.views') dijalankan.

  3. 4Pyramid mengimpor mypackage.views.py, menemukan @view_config(route_name='hello') di atas hello_world.

  4. Pyramid secara internal melakukan hal yang sama dengan config.add_view('mypackage.views.hello_world', route_name='hello') untuk kita.

  5. Aplikasi berjalan seperti biasa.

* Masalah/Error: Tidak ada error.

### 5. Kesimpulan
Menggunakan @view_config membuat kode lebih rapi. Logika view (fungsi itu sendiri) dan konfigurasi view (untuk rute apa dia?) sekarang berada di satu tempat yang sama (yaitu di file views.py). Ini lebih mudah dibaca dan dikelola daripada harus bolak-balik antara views.py dan __init__.py.