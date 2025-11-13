# Analisis Percobaan 09: Organizing Views With View Classes

### 1. Tujuan Percobaan
Tujuan percobaan ini adalah untuk me-*refactor* kode *view* kita dari *view function* (fungsi biasa) menjadi *view class* (sebuah *class* yang berisi *method-method* *view*). Ini adalah pola desain yang lebih terorganisir untuk aplikasi yang lebih besar.

### 2. Kode Program Utama
(Tempelkan kode dari `mypackage/views.py` di sini)
```python
from pyramid.view import view_config

class TutorialViews:
    def __init__(self, request):
        """
        Constructor ini otomatis dipanggil oleh Pyramid saat
        request masuk. 'request' di-inject secara otomatis.
        """
        self.request = request
        # Kita bisa siapkan data di sini
        self.greeting = request.registry.settings['app_greeting']

    @view_config(route_name='hello', renderer='mypackage:hello.pt')
    def hello_world(self):
        """
        Ini adalah view method kita. Pyramid akan memanggil ini.
        """
        print('Incoming request (CLASS-BASED), rendering template...')
        return {'greeting': self.greeting}
```

### 3. Hasil Percobaan (Screenshot)
<img width="960" height="1137" alt="Image" src="https://github.com/user-attachments/assets/d6f2cad5-4b74-44aa-95a1-a5da7daa167f" />
<img width="1917" height="1089" alt="Image" src="https://github.com/user-attachments/assets/62320586-236f-414a-a08d-2800c3b38d50" />

### 4. Analisis
* Konsep Utama: View Class. Alih-alih mendaftarkan fungsi, kita mendaftarkan method dari sebuah class.

* Cara Kerja:

  1. config.scan('.views') di __init__.py memindai views.py.

  2. Pyramid menemukan class TutorialViews dan melihat bahwa method hello_world di dalamnya memiliki decorator @view_config(route_name='hello').

  3. Pyramid mendaftarkan method ini untuk rute 'hello'.

  4. Saat request masuk ke /, Pyramid secara otomatis membuat instance dari class tersebut: instance = TutorialViews(request). Constructor __init__ dipanggil, menyimpan self.request dan self.greeting.

  5. Pyramid kemudian memanggil method yang terdaftar: instance.hello_world().

  6. Method ini mengembalikan dictionary {'greeting': self.greeting}, yang kemudian di-render oleh hello.pt seperti sebelumnya.

* Poin Penting Tes: Functional test kita di test_views.py lulus tanpa diubah sama sekali. Ini karena functional test tidak peduli bagaimana view diimplementasikan (fungsi atau class); ia hanya peduli bahwa GET ke / mengembalikan HTML yang benar.

* Masalah/Error: Tidak ada masalah.

5. Kesimpulan
View class adalah cara yang sangat rapi untuk mengelompokkan view yang saling terkait. Kita bisa berbagi logika di dalam __init__ (seperti mengambil data user, koneksi database, dll) dan menggunakannya di semua method view di dalam class tersebut.