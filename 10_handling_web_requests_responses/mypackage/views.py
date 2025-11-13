from pyramid.view import view_config

class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.greeting = request.registry.settings['app_greeting']

    @view_config(route_name='hello', renderer='mypackage:hello.pt')
    def hello_world(self):
        print('Incoming request, handling request/response...')
        
        name = self.request.params.get('name', 'No Name')

        return {
            'greeting': self.greeting,
            'name': name,
            'path': self.request.path, 
        }