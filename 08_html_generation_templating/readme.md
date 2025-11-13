# Analisis Percobaan 08: HTML Generation With Templating

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk memisahkan logika (Python) dari presentasi (HTML) menggunakan *template engine*. Kita belajar menggunakan *renderer* yang menunjuk ke file template (`.pt`), dan mengubah *view* kita untuk me-return *dictionary* data, bukan objek `Response`.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/views.py` di sini)
```python
from pyramid.view import view_config

@view_config(route_name='hello', renderer='mypackage:hello.pt')
def hello_world(request):
    
    greeting = request.registry.settings['app_greeting']
    print('Incoming request, rendering template...')
    
    # View sekarang me-return dictionary
    return {'greeting': greeting}
```

### 3. Hasil Percobaan (Screenshot)
<img width="959" height="1139" alt="Image" src="https://github.com/user-attachments/assets/9a53c54c-0302-4cf8-a481-b35a7ec849db" />
<img width="1871" height="1093" alt="Image" src="https://github.com/user-attachments/assets/096c39cd-d40f-49f8-9ac2-5811f7462237" />

### 4. Analisis
* Konsep Utama: Renderers dan Pemisahan Lojik.

* renderer='mypackage:hello.pt': Ini adalah asset spec yang kita tambahkan di @view_config. Ini memberitahu Pyramid: "Jangan repot-repot, setelah fungsi ini selesai, ambil dictionary yang di-return, dan gunakan renderer hello.pt untuk mengubahnya menjadi HTML".

* Pemisahan Lojik: File views.py kita sekarang murni berisi logika Python (mendapatkan data greeting). File hello.pt murni berisi presentasi HTML. Ini membuat keduanya lebih mudah dikelola.

* return {'greeting': greeting}: Kunci ('greeting') dalam dictionary ini secara otomatis menjadi variabel (${greeting}) di dalam template Chameleon.

* Cara Kerja:

  1. config.include('pyramid_chameleon') mendaftarkan template engine Chameleon.

  2. Request masuk ke /. Pyramid mencocokkan ke hello_world via @view_config.

  3. Fungsi hello_world dieksekusi, mengambil data greeting, dan me-return dictionary: {'greeting': 'Hello from .ini!'}.

  4. Pyramid melihat ada renderer yang terdaftar. Pyramid tidak langsung mengirim dictionary itu.

  5. Pyramid memanggil renderer hello.pt, memberinya dictionary tadi.

  6. Chameleon mem-parsing hello.pt, mengganti ${greeting} dengan "Hello from .ini!", dan menghasilkan HTML final.

  7. HTML final inilah yang dikirim sebagai Response ke browser.

* Masalah/Error: Tidak ada masalah ataupun error.

5. Kesimpulan
Menggunakan renderers dan template adalah cara standar dalam web development. Ini membuat kode view kita lebih bersih (hanya fokus pada data) dan kode HTML kita terorganisir di file terpisah, sehingga desainer web dan backend developer bisa bekerja paralel.