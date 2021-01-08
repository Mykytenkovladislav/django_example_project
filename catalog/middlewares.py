from models import StoredRequests


class LogMiddleware:  # TODO Fix middleware and  his import
    def __init__(self, get_response):
        self.get_response = get_response

    # One-time configuration and initialization.

    def __call__(self, request):
        response = self.process_request(request)
        if response is None:
            response = self.get_response(request)
        return response

    def process_request(self, request):
        request_obj = StoredRequests(path=request.method, method=request.get_full_path())
        request_obj.save()
        return request
