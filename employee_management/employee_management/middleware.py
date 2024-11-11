from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

from users.models import BlackListedIPAddresses


class GetIPAddressesMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))


from django.http import HttpResponseForbidden

BLOCKED_IPS = {'192.168.1.10', '203.0.113.5'}

class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        if client_ip in BLOCKED_IPS:
            return HttpResponseForbidden("Your IP is blocked.")
        return self.get_response(request)
