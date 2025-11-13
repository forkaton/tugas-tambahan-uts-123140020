from pyramid.view import view_config

class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.greeting = request.registry.settings['app_greeting']

    @view_config(route_name='home', renderer='home.jinja2') 
    def home_view(self):
        print('Incoming request (home), rendering JINJA2...')
        name = self.request.params.get('name', 'No Name')
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path,
        }

    @view_config(route_name='hello', renderer='hello.jinja2') 
    def hello_view(self):
        print('Incoming request (hello dynamic), rendering JINJA2...')
        name = self.request.matchdict['name']
        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path,
        }