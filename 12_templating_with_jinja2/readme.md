# Analisis Percobaan 12: Templating With jinja2

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari cara mengganti *template engine* bawaan (Chameleon) dengan *engine* lain yang populer, yaitu Jinja2. Ini menunjukkan fleksibilitas Pyramid dalam hal *plug-and-play*.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/__init__.py` di sini)
```python
from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        # Ganti Chameleon dengan Jinja2
        config.include('pyramid_jinja2')
        
        # Beri tahu Jinja2 di mana folder template kita
        config.add_jinja2_search_path('mypackage:templates')
        
        greeting = settings.get('app_greeting', 'Hello from .ini!')
        config.registry.settings['app_greeting'] = greeting

        config.add_route('home', '/')
        config.add_route('hello', '/hello/{name}')

        config.scan('.views') 
        
        return config.make_wsgi_app()
```

### 3. Hasil Percobaan (Screenshot)
<img width="958" height="1093" alt="Image" src="https://github.com/user-attachments/assets/2984393f-1316-4eb1-b3ef-20f48c9f887e" />
<img width="1914" height="1095" alt="Image" src="https://github.com/user-attachments/assets/d96cddb4-a397-4c1d-9150-4c65745fb523" />

### 4. Analisis
* Konsep Utama: Pluggable Template Engines.

* Perubahan setup.py: Kita mengganti pyramid_chameleon dengan pyramid_jinja2 untuk mengubah dependency.

* config.include('pyramid_jinja2'): Perintah ini "memuat" plugin Jinja2 ke dalam aplikasi kita.

* config.add_jinja2_search_path(...): Perintah ini memberi tahu Jinja2, "Setiap kali view meminta template (seperti home.jinja2), carilah di dalam folder mypackage/templates".

* Struktur Folder: Jinja2 (secara konvensi) lebih menyukai semua template berada di satu folder templates/.

* Sintaks: Sintaks Chameleon (${...}) diganti dengan sintaks Jinja2 ({{ ... }}).

* renderer='home.jinja2': Di dalam view, kita sekarang hanya perlu menentukan nama file template. Pyramid dan pyramid_jinja2 akan menemukannya berkat search path yang telah diatur.

* Masalah/Error: Tidak ada Error maupun Masalah

### 5. Kesimpulan
Pyramid tidak memaksakan satu template engine. Kita bisa dengan mudah menukar Chameleon dengan Jinja2 (atau Mako, dll.) hanya dengan mengubah beberapa baris konfigurasi. Ini menunjukkan filosofi Pyramid yang fleksibel dan tidak memihak.