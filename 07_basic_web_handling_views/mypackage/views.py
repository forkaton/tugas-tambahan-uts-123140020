from pyramid.response import Response
from pyramid.view import view_config # <-- IMPOR INI

# @view_config memberi tahu Pyramid bahwa ini adalah view
# 'route_name='hello'' menghubungkannya ke rute 'hello'
@view_config(route_name='hello') # <-- TAMBAHKAN DECORATOR INI
def hello_world(request):
    # Ambil nilai 'app_greeting' dari registry
    greeting = request.registry.settings['app_greeting']
    
    print('Incoming request, greeting is:', greeting)
    return Response(greeting)