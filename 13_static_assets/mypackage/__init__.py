from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.add_jinja2_search_path('mypackage:templates')
        config.add_static_view(name='static', path='mypackage:static')
        # Ini berarti URL /static/style.css akan
        # mengambil file dari mypackage/static/style.css

        greeting = settings.get('app_greeting', 'Hello from .ini!')
        config.registry.settings['app_greeting'] = greeting

        config.add_route('home', '/')
        config.add_route('hello', '/hello/{name}')
        config.scan('.views') 
        
        return config.make_wsgi_app()