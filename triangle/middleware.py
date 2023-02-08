from django.urls import reverse

from .models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        admin_url = reverse('admin:index')
        if admin_url not in request.path:
            data = {}
            query = request.GET
            if request.method != 'GET':
                data = request.POST

            log = Log(path=request.path, method=request.method, data=data, query=query)
            log.save()
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
