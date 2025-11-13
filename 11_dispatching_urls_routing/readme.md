# Analisis Percobaan 11: Dispatching URLs To Views With Routing

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari *dynamic routing*. Kita belajar cara mendefinisikan "placeholder" di dalam pola URL (cth: `/hello/{name}`) dan cara mengambil nilai dari *placeholder* tersebut di dalam *view* menggunakan `request.matchdict`.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/views.py` di sini)
```python
from pyramid.view import view_config

class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.greeting = request.registry.settings['app_greeting']

    @view_config(route_name='home', renderer='mypackage:home.pt')
    def home_view(self):
        name = self.request.params.get('name', 'No Name')
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path,
        }

    @view_config(route_name='hello', renderer='mypackage:hello.pt')
    def hello_view(self):
        # Ambil 'name' dari 'matchdict'
        name = self.request.matchdict['name']
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path,
        }
```

### 3. Hasil Percobaan (Screenshot)
<img width="959" height="1137" alt="Image" src="https://github.com/user-attachments/assets/a1b2051a-ee83-4490-8c92-4c2dd47e806d" />
<img width="1910" height="1086" alt="Image" src="https://github.com/user-attachments/assets/54bd10e2-a1df-451b-b319-d75a5f22dbc9" />

### 4. Analisis
* Konsep Utama: Dynamic Routing dan request.matchdict.

* config.add_route('hello', '/hello/{name}'): Bagian {name} adalah placeholder dinamis. Pyramid akan mencocokkan URL apapun yang polanya /hello/sesuatu.

* request.params (Tutorial 10): Mengambil data dari query string (?name=Ansel).

* request.matchdict (Tutorial 11): Mengambil data dari path URL (/hello/Ansel). Ini adalah dictionary di mana key-nya adalah nama placeholder (yaitu 'name') dan value-nya adalah apa yang dicocokkan di URL (yaitu 'Ansel').

* Cara Kerja:

  1. Dua rute didaftarkan: home (untuk /) dan hello (untuk /hello/{name}).

  2. Jika request masuk ke /, rute home cocok. Pyramid memanggil home_view, yang menggunakan request.params (logika lama).

  3. Jika request masuk ke /hello/Ansel, rute hello cocok. Pyramid tahu bahwa name = 'Ansel'.

  4. Pyramid memanggil hello_view. Di dalam view ini, kita mengakses self.request.matchdict['name'], yang mengembalikan nilai 'Ansel'.

  5. Nilai 'Ansel' ini dikirim ke template hello.pt dan di-render.

* Masalah/Error: Tidak ada error.

5. Kesimpulan
matchdict dan dynamic routing adalah cara standar untuk membuat URL yang bersih dan mudah dibaca (RESTful). Ini memisahkan data (seperti ID atau nama) dari query string dan memasukkannya langsung ke path URL, yang lebih intuitif.