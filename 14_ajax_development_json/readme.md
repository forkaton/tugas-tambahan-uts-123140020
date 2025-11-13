# Analisis Percobaan 14: AJAX Development With JSON Renderers

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk mempelajari cara membuat *API endpoint* yang mengembalikan data dalam format JSON. Kita menggunakan *renderer* `json` bawaan Pyramid untuk secara otomatis mengubah *dictionary* Python menjadi respons JSON.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/views.py` di sini, fokus pada *view* JSON baru)
```python
    @view_config(route_name='hello_json', renderer='json')
    def hello_json_view(self):
        """ View ini mengembalikan data JSON. """
        print('Incoming request (JSON API)...')
        name = self.request.matchdict['name']
        
        # Sama seperti view lain, kita return dictionary.
        # TAPI, karena 'renderer="json"', Pyramid akan
        # mengubah dictionary ini menjadi string JSON.
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path,
        }
```

### 3. Hasil Percobaan (Screenshot)
<img width="954" height="1086" alt="Image" src="https://github.com/user-attachments/assets/a44e07b9-a905-43a7-b024-365569d6867c" />
<img width="1912" height="1095" alt="Image" src="https://github.com/user-attachments/assets/be960843-97b7-4aa7-8924-915f0fd0bcaf" />

### 4. Analisis
* Konsep Utama: renderer='json'.

* Pemisahan Data dan Tampilan: Ini adalah pemisahan total. View HTML (Tutorial 13) menggabungkan data (Python) dengan template (HTML). View JSON ini hanya mengirim data mentah. Terserah client (bisa jadi JavaScript, aplikasi mobile, atau script lain) mau diapakan data ini.

* Otomatisasi: Kita hanya me-return dictionary Python biasa. Decorator renderer='json' memberitahu Pyramid untuk:

* Mengambil dictionary itu.

* Menjalankan json.dumps() (serialisasi) di baliknya.

* Membuat objek Response baru.

* Mengatur header Content-Type menjadi application/json.

* Mengirim respons itu ke client.

* WebTest.json: Di testing, kita tidak lagi memeriksa HTML (response.html). Kita menggunakan response.json, yang secara otomatis mem-parsing string JSON kembali menjadi dictionary Python untuk diuji.

* Masalah/Error: Tidak ada error pada program.

### 5. Kesimpulan
Renderer JSON adalah alat yang sangat kuat dan sederhana di Pyramid. Hanya dengan satu kata kunci di decorator (renderer='json'), kita bisa membuat API endpoint yang robust dan siap dikonsumsi oleh aplikasi lain (seperti frontend JavaScript, aplikasi Android/iOS, dll).