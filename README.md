django-redis-countries
======================

Installation
------------

Add ```redis_countries``` to your INSTALLED_APPS:
```
INSTALLED_APPS = (
    ...
    'redis_countries',
    ...
)
```

Add the RedisCountryCodeMiddleware to your MIDDLEWARE_CLASSES:
```
MIDDLEWARE_CLASSES = (
    ...
    'redis_countries.middleware.RedisCountryCodeMiddleware',
    ...
)
```

Usage
-----

In order to user django-redis-countries you need to download the database

You can find it in http://dev.maxmind.com/geoip/legacy/geolite/

Download the CSV/ZIP version of the database called **GeoLite Country** and unzip it

TODO
----

- Automatically download the appropiate database for MaxMind's website (Actually see if that is legal).
- Add more information to the request objects
- IPv6
