# Analisis Percobaan 04: Easier Development with debugtoolbar

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari cara mengaktifkan dan menggunakan `pyramid_debugtoolbar`, sebuah alat bantu *debugging* yang sangat berguna dalam proses pengembangan.

### 2. Kode Program Utama
(Tempelkan kode dari `development.ini` di sini karena itu intinya)
```ini
[app:main]
use = egg:mypackage#main
app_greeting = Hello from .ini!
pyramid.includes = pyramid_debugtoolbar

[server:main]
use = egg:waitress#main
host = 0.0.0.0
port = 6543
```

### 3. Hasil Percobaan (Screenshot)
<img width="1873" height="1091" alt="Image" src="https://github.com/user-attachments/assets/97169f46-564b-431c-be00-66bf2f93cf89" />

### 4. Analisis
* Konsep Utama: Debugging dan Extensibility (kemampuan diperluas). Pyramid memiliki sistem include yang memudahkan kita menambah fungsionalitas (seperti debug toolbar) hanya dengan mengubah konfigurasi.

* Cara Kerja:

  1. Dengan menambahkan pyramid_debugtoolbar ke setup.py, kita memastikan library itu ter-install di virtual environment.

  2. Dengan menambahkan pyramid.includes = pyramid_debugtoolbar di file .ini, kita memberi tahu Configurator Pyramid untuk memuat plugin tersebut saat aplikasi dimulai.

  3. Saat kita mengakses aplikasi di browser, toolbar ini secara otomatis menyuntikkan dirinya ke halaman HTML yang dikirim, muncul sebagai overlay di sisi kanan.

  4. Toolbar ini memberi kita akses instan ke informasi request, logging, settings, dan profiler performa tanpa perlu print() manual.

* Masalah/Error: Tidak ada masalah atau error.

### 5. Kesimpulan
pyramid_debugtoolbar adalah alat yang sangat penting untuk pengembangan. Hanya dengan dua baris konfigurasi (satu di setup.py dan satu di .ini), kita mendapatkan alat debugging interaktif yang mempercepat proses pencarian masalah.