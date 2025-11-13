from pyramid.response import Response

def hello_world(request):
    # Ambil nilai 'app_greeting' dari registry
    greeting = request.registry.settings['app_greeting']
    
    print('Incoming request, greeting is:', greeting)
    return Response(greeting)