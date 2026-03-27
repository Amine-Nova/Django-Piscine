import json
from django.core.management.base import BaseCommand
from ex10.models import Planets, People, Movies
import warnings

class Command(BaseCommand):
    help = "Load JSON fixture fixing numeric homeworld IDs to names"

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON fixture')

    def handle(self, *args, **options):
        try:
            warnings.filterwarnings(
                "ignore",
                category=RuntimeWarning,
            )
            json_file = options['json_file']

            with open(json_file, 'r') as f:
                data = json.load(f)

            for obj in data:
                if obj['model'].lower().endswith('planets'):
                    Planets.objects.update_or_create(
                        pk=obj['pk'],
                        defaults=obj['fields']
                    )
                elif obj['model'].lower().endswith('people'):
                    planets_fields = list(obj['fields'].values())
                    if planets_fields[7]:
                        homeworld = Planets.objects.get(pk=planets_fields[7])
                    else:
                        homeworld = None
                    People.objects.update_or_create(
                        pk=obj['pk'],
                        name=planets_fields[0],
                        birth_year=planets_fields[1],
                        gender=planets_fields[2],
                        eye_color=planets_fields[3],
                        hair_color=planets_fields[4],
                        height=planets_fields[5],
                        mass=planets_fields[6],                  
                        homeworld=homeworld,
                    )
                elif obj['model'].lower().endswith('movies'):
                    movies_fields = list(obj['fields'].values())
                    get_characters = People.objects.filter(pk__in=movies_fields[5])
                    character, created = Movies.objects.update_or_create(
                        pk=obj['pk'],
                        title=movies_fields[0],
                        opening_crawl=movies_fields[1],
                        director=movies_fields[2],
                        producer=movies_fields[3],
                        release_date=movies_fields[4],
                    )
                    character.characters.set(get_characters)
            self.stdout.write(self.style.SUCCESS('Insertion Successfull!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))