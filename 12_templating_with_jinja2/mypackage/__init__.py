from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        # config.include('pyramid_chameleon') 
        config.include('pyramid_jinja2')  
        
        # Beri tahu Jinja2 di mana folder template kita
        config.add_jinja2_search_path('mypackage:templates')
        
        # ... (kode greeting tetap sama) ...
        greeting = settings.get('app_greeting', 'Hello from .ini!')
        config.registry.settings['app_greeting'] = greeting

        # ... (kode routing tetap sama) ...
        config.add_route('home', '/')
        config.add_route('hello', '/hello/{name}')

        config.scan('.views') 
        
        return config.make_wsgi_app()