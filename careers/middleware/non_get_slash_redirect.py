from django.http import HttpResponsePermanentRedirect


class NonGetSlashRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.endswith('/') and request.method != 'GET':
            request.path_info = request.path + '/'
        return self.get_response(request)