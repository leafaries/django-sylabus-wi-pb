from django.utils import translation

class URLOnlyLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        if path.startswith('/en/'):
            language = 'en'
        else:
            language = 'pl'

        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()

        response = self.get_response(request)

        response['Content-Language'] = translation.get_language()
        return response
