from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound # <-- IMPOR INI

class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.greeting = request.registry.settings['app_greeting']

    # ... (home_view, hello_view, hello_json_view tetap ada) ...
    @view_config(route_name='home', renderer='home.jinja2')
    def home_view(self):
        # ... (kode lama) ...
        return {
            'greeting': self.greeting,
            'name': 'No Name',
            'path': self.request.path,
        }

    @view_config(route_name='hello', renderer='hello.jinja2')
    def hello_view(self):
        # ... (kode lama) ...
        name = self.request.matchdict['name']
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path,
        }

    @view_config(route_name='hello_json', renderer='json')
    def hello_json_view(self):
        # ... (kode lama) ...
        name = self.request.matchdict['name']
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path,
        }

    @view_config(
        route_name='hello_edit',
        renderer='edit.jinja2',
        request_method='GET'  
    )
    def edit_view(self):
        """ Menampilkan form edit. """
        print('Incoming GET request to edit_view...')
        name = self.request.matchdict['name']
        return {
            'name': name,
            'greeting': self.greeting
        }

    @view_config(
        route_name='hello_edit',
        request_method='POST' 
    )
    def edit_process_view(self):
        """ Memproses data form yang disubmit. """
        print('Incoming POST request to edit_process_view...')
        name = self.request.matchdict['name']
        
        # Ambil data form dari 'new_greeting'
        new_greeting = self.request.params.get('new_greeting')
        
        # (Di aplikasi nyata, kita akan simpan ini ke database)
        # Untuk sekarang, kita simpan kembali ke settings:
        self.request.registry.settings['app_greeting'] = new_greeting
        
        # Redirect kembali ke halaman hello_view
        redirect_url = self.request.route_url('hello', name=name)
        return HTTPFound(redirect_url)