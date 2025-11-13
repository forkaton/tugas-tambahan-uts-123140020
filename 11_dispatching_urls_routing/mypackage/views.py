from pyramid.view import view_config

class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.greeting = request.registry.settings['app_greeting']

    @view_config(route_name='home', renderer='mypackage:home.pt') # <-- UBAH INI
    def home_view(self):
        print('Incoming request (home), rendering template...')
        
        # Logika ini sama seperti tutorial 10 (dari query string)
        name = self.request.params.get('name', 'No Name')
        
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path,
        }

    @view_config(route_name='hello', renderer='mypackage:hello.pt') # <-- TAMBAH METHOD INI
    def hello_view(self):
        print('Incoming request (hello dynamic), rendering template...')
        
        name = self.request.matchdict['name']
        
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path,
        }