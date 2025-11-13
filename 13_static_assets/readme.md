# Analisis Percobaan 13: CSS/JS/Images Files With Static Assets

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari cara menyajikan *static assets* (file seperti CSS, JavaScript, dan gambar) menggunakan Pyramid.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/__init__.py` di sini, fokus pada `add_static_view`)
```python
from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.add_jinja2_search_path('mypackage:templates')
        
        # Daftarkan 'static' sebagai URL path
        # 'mypackage:static' adalah asset spec ke folder
        config.add_static_view(name='static', path='mypackage:static')
        
        # ... (sisa kode) ...
        
        config.add_route('home', '/')
        config.add_route('hello', '/hello/{name}')
        config.scan('.views') 
        
        return config.make_wsgi_app()
```

### 3. Hasil Percobaan (Screenshot)
<img width="956" height="1137" alt="Image" src="https://github.com/user-attachments/assets/0d1acf9e-9e22-49d4-a9b0-436975e72f36" />
<img width="1917" height="1081" alt="Image" src="https://github.com/user-attachments/assets/7d33e5b9-3283-4c1e-9f04-13aa6830e773" />

### 4. Analisis
* Konsep Utama: Static View.

* config.add_static_view(...): Ini adalah perintah kuncinya. Perintah ini memberitahu Pyramid untuk membuat view khusus yang tidak menjalankan kode Python, tapi hanya menyajikan file langsung dari filesystem.

* name='static': Ini mendefinisikan URL endpoint. Ini berarti semua file di bawah folder static akan bisa diakses melalui URL http://localhost:6543/static/nama-file.

* path='mypackage:static': Ini adalah asset spec yang memberitahu Pyramid di folder filesystem mana file-file itu berada (yaitu di mypackage/static/).

* request.static_url(...): Ini adalah helper di template. Kita tidak menulis URL /static/style.css secara hardcode. Mengapa? Karena jika suatu hari kita mengubah name dari 'static' menjadi 'assets', kita hanya perlu mengubahnya di __init__.py, dan template akan otomatis ter-update.

* Masalah/Error: Tidak ada masalah pada program.

### 5. Kesimpulan
Menyajikan file statis adalah kebutuhan dasar web. Pyramid menangani ini dengan add_static_view, yang secara efisien memetakan sebuah URL ke sebuah folder di disk. Menggunakan request.static_url di template adalah praktik terbaik untuk memastikan URL aset kita selalu benar.