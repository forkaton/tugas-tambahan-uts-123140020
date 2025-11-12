from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        # Baca setting 'app_greeting' dari file .ini
        # Jika tidak ada, gunakan 'Hello World!' sebagai default
        greeting = settings.get('app_greeting', 'Hello World!')
        
        # Simpan nilai greeting ke registry config
        config.registry.settings['app_greeting'] = greeting

        config.add_route('hello', '/')
        # Arahkan ke view yang sama, tapi view-nya nanti kita ubah
        config.add_view('mypackage.views.hello_world', route_name='hello')
        return config.make_wsgi_app()