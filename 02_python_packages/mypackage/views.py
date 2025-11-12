from pyramid.response import Response

def hello_world(request):
    print('Incoming request')
    return Response('Hello World!')