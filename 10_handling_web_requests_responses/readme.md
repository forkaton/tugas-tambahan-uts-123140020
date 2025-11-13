# Analisis Percobaan 10: Handling Web Requests and Responses

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk memahami lebih dalam objek `request`. Secara spesifik, kita belajar cara membaca data dari *query string* (parameter URL) menggunakan `request.params` dan meneruskannya ke *template*.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/views.py` di sini)
```python
from pyramid.view import view_config

class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.greeting = request.registry.settings['app_greeting']

    @view_config(route_name='hello', renderer='mypackage:hello.pt')
    def hello_world(self):
        print('Incoming request, handling request/response...')
        
        # Ambil 'name' dari query string, cth: /?name=Ansel
        name = self.request.params.get('name', 'No Name')
        
        # Kirim lebih banyak data ke template
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path, # Mengirim URL path (cth: '/')
        }
```
### 3. Hasil Percobaan (Screenshot)
<img width="960" height="1145" alt="Image" src="https://github.com/user-attachments/assets/b336a1e6-fdb6-464a-beec-9064c6e2d663" />
<img width="1918" height="1088" alt="Image" src="https://github.com/user-attachments/assets/05e4e3c1-3f12-450d-a109-482497620b10" />

### 4. Analisis
* Konsep Utama: Objek request sebagai sumber data.

* request.params: Ini adalah properti terpenting. Ini adalah objek mirip dictionary yang berisi gabungan data dari URL query string (GET) dan form body (POST).

* request.params.get('name', 'No Name'): Ini adalah cara aman untuk mengambil data. "Coba dapatkan key 'name'. Jika tidak ada (None), kembalikan nilai default 'No Name'". Ini mencegah aplikasi kita crash jika parameter name tidak ada.

* request.path: Properti ini berisi bagian path dari URL, tidak termasuk host atau query string. Berguna untuk mengetahui halaman apa yang sedang diakses.

* Objek Response: Meskipun kita tidak membuat objek Response secara manual (karena renderer yang melakukannya), kita secara implisit mengontrolnya. Renderer akan mengambil dictionary kita dan membuat Response dengan body berupa HTML dan status 200 OK.

* Masalah/Error: Tidak ada Error maupun Masalah

5. Kesimpulan
Objek request adalah jembatan utama antara pengguna (browser) dan aplikasi kita. Memahami cara "membongkar" request.params adalah fundamental untuk membuat aplikasi web interaktif yang bisa merespons input pengguna, baik dari URL maupun dari form.