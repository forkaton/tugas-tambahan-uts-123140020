# Analisis Percobaan 15: More With View Classes

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari cara menggunakan satu rute (URL) untuk menangani beberapa *HTTP method* (GET dan POST). Kita menggunakan *view predicate* `request_method` untuk memetakan *request* yang berbeda ke *view method* yang berbeda di dalam *class* yang sama.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/views.py` di sini, fokus pada dua *view* baru)
```python
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound # <-- Impor

    # ... (view-view lama) ...

    @view_config(
        route_name='hello_edit',
        renderer='edit.jinja2',
        request_method='GET'  # <-- HANYA merespon GET
    )
    def edit_view(self):
        """ Menampilkan form edit. """
        name = self.request.matchdict['name']
        return { 'name': name, 'greeting': self.greeting }

    @view_config(
        route_name='hello_edit',
        request_method='POST' # <-- HANYA merespon POST
    )
    def edit_process_view(self):
        """ Memproses data form yang disubmit. """
        name = self.request.matchdict['name']
        new_greeting = self.request.params.get('new_greeting')
        
        self.request.registry.settings['app_greeting'] = new_greeting
        
        # Redirect kembali ke halaman hello_view
        redirect_url = self.request.route_url('hello', name=name)
        return HTTPFound(redirect_url)
```

### 3. Hasil Percobaan (Screenshot)
* Dokumentasi 5 Pass ketika pytest di terminal
<img width="960" height="1141" alt="Image" src="https://github.com/user-attachments/assets/1a1eed22-297f-4e00-b5a7-695de3df9c40" />

* Dokumentasi browser dan alur PRG mulai dari merubah isi form, save, hingga menampilkan header baru
<img width="1917" height="1084" alt="Image" src="https://github.com/user-attachments/assets/11cb093f-25e4-4761-a23d-cdc8499bdd8b" />
<img width="1918" height="1087" alt="Image" src="https://github.com/user-attachments/assets/be6ff57a-eace-417c-80a4-d9ea7ba98ddd" />
<img width="1916" height="1086" alt="Image" src="https://github.com/user-attachments/assets/59e886c4-fdb3-4f40-9b8e-9fd9df8b29d1" />

### 4. Analisis
* Konsep Utama: View Predicates dan Post/Redirect/Get (PRG).

* request_method='GET': Ini adalah predicate. Ini memberitahu Pyramid: "Untuk rute 'hello_edit', jika request-nya adalah GET, panggil method edit_view."

* request_method='POST': Predicate ini memberitahu Pyramid: "Untuk rute 'hello_edit', jika request-nya adalah POST, panggil method edit_process_view."

* Pola PRG: Ini adalah pola desain web yang penting.

* POST: Client mengirim data (edit_process_view).

* REDIRECT: Server memproses data dan merespons dengan redirect (HTTPFound) ke halaman lain.

* GET: Browser client secara otomatis mengikuti redirect dan membuat request GET baru ke halaman hasil (hello_view).

* Penggunaan PRG untuk mencegah pengguna men-submit form yang sama dua kali jika mereka menekan tombol refresh di browser setelah submit.

* Masalah/Error: Program berjalan dengan baik tanpa masalah ataupun error.

### 5. Kesimpulan
View predicate (seperti request_method) adalah fitur yang sangat kuat di Pyramid. Ini memungkinkan kita mengorganisir logika kita dengan rapi, di mana satu URL bisa memiliki beberapa view berbeda yang menanganinya, tergantung pada konteks request (metode, header, dll).