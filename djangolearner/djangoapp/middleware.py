class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f'LoggingMiddleware executed, IP: {request.META['REMOTE_ADDR']}')
        response = self.get_response(request)
        return response