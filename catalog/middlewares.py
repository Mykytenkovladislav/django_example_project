from catalog.models import StoredRequest


class LogMiddleware:  # TODO Fix middleware and  his import
    def __init__(self, get_response):
        self.get_response = get_response

    # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request_obj = StoredRequest(path=request.get_full_path(), method=request.method)
        request_obj.save()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
