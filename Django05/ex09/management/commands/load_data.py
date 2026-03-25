import json
from django.core.management.base import BaseCommand
from ex09.models import Planets, People
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
                    up = list(obj['fields'].values())
                    if up[7]:
                        homeworld = Planets.objects.get(pk=up[7])
                    else:
                        homeworld = None
                    People.objects.update_or_create(
                        pk=obj['pk'],
                        name=up[0],
                        birth_year=up[1],
                        gender=up[2],
                        eye_color=up[3],
                        hair_color=up[4],
                        height=up[5],
                        mass=up[6],                  
                        homeworld=homeworld,
                        created=up[8],
                        updated=up[9],
                    )
            self.stdout.write(self.style.SUCCESS('Insertion Successfull!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))