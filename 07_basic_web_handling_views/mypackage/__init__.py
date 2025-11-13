from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        # Baca setting 'app_greeting' dari file .ini
        greeting = settings.get('app_greeting', 'Hello from .ini!')
        
        # Simpan nilai greeting ke registry config
        config.registry.settings['app_greeting'] = greeting

        config.add_route('hello', '/')
        
        # Perubahan Kunci:
        # Kita tidak lagi memanggil config.add_view() di sini.
        # Sebagai gantinya, kita memindai (scan) package untuk
        # menemukan decorator @view_config.
        config.scan('.views') 
        
        return config.make_wsgi_app()