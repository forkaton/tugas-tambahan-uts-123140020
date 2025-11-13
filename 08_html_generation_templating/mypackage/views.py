from pyramid.view import view_config

@view_config(route_name='hello', renderer='mypackage:hello.pt') 
def hello_world(request):
    
    greeting = request.registry.settings['app_greeting']
    print('Incoming request, rendering template...')
    
    # Dulu: return Response(greeting)
    # Sekarang: return Dictionary.
    # Kunci 'greeting' di sini HARUS cocok dengan ${greeting} di file .pt
    return {'greeting': greeting}