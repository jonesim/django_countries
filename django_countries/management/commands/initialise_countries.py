import csv
import inspect
from django.core.management.base import BaseCommand
import country
from country.models import Country


def initialise_countries():
    country_path = '/'.join(inspect.getfile(country).split('/')[:-1])
    f = open(country_path + '/data/countries.csv')
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        new_country = Country(iso_code=r[0], name=r[3])
        new_country.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        initialise_countries()
