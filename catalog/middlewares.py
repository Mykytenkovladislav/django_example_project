from catalog.models import StoredRequests


class LogMiddleware:  # TODO Fix middleware and  his import
    def __init__(self, get_response):
        self.get_response = get_response

    # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request_obj = StoredRequests(path=request.get_full_path(), method=request.method)
        request_obj.save()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    # def process_request(self, request):
    #     request_obj = StoredRequests(path=request.method, method=request.get_full_path())
    #     request_obj.save()
    #     return request
