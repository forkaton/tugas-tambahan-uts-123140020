from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        
        config.include('pyramid_chameleon') # <-- TAMBAHKAN INI
        
        # ... (kode greeting tetap sama) ...
        greeting = settings.get('app_greeting', 'Hello from .ini!')
        config.registry.settings['app_greeting'] = greeting

        config.add_route('hello', '/')
        config.scan('.views') 
        
        return config.make_wsgi_app()