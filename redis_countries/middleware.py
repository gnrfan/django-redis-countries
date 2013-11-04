from django.http import HttpResponsePermanentRedirect
from django.conf import settings
from redis_countries import RedisCountries

DEFAULT_COUNTRY = getattr(settings, "DEFAULT_CLIENT_COUNTRY", None)

class RedisCountryCodeMiddleware(object):
    """Adds a 'country_code' parameter to the request object."""
    def __init__(self, *args, **kwargs):
        self.conn = RedisCountries()
        super(RedisCountryCodeMiddleware, self).__init__(*args, **kwargs)

    def process_request(self, request):
        client_address = request.META.get('REMOTE_ADDR', None)
        request.country_code = self.conn.get_country_code(client_address,
                                                          DEFAULT_COUNTRY)
