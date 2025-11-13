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
        Perhatikan @view_config sekarang ada di method, bukan di atas class.
        """
        print('Incoming request (CLASS-BASED), rendering template...')
        
        # Kembalikan dictionary seperti sebelumnya
        return {'greeting': self.greeting}

