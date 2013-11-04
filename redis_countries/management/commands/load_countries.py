# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand

from redis_countries import RedisCountries


class Command(BaseCommand):
    """"""
    def handle(self, *args, **kwargs):
        if len(args) < 1:
            print "Please specify csv file containing the data."
            return
        redis_countries = RedisCountries()
        redis_countries.import_data(args[0])
