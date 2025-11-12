from pyramid.config import Configurator

def main(global_config, **settings):
    """ Fungsi ini mengembalikan aplikasi WSGI.
    """
    with Configurator(settings=settings) as config:
        config.add_route('hello', '/')
        config.add_view('mypackage.views.hello_world', route_name='hello')
        return config.make_wsgi_app()