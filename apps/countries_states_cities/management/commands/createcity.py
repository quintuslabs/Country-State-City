from django.core.management.base import BaseCommand

from apps.countries_states_cities.models import City


class Command(BaseCommand):
    help = "Enter the city details"

    @staticmethod
    def handle(*args, **options):
        print("Creating cities...")
        country = 1
        state = 2
        cities = [
            "Baleshwar",
            "Dehradun",
            "Haldwani-cum-Kathgodam",
            "Hardwar",
            "Kashipur",
            "Manglaur",
            "Mussoorie",
            "Nagla",
            "Nainital",
            "Pauri",
            "Pithoragarh",
            "Ramnagar",
            "Rishikesh",
            "Roorkee",
            "Rudrapur",
            "Sitarganj",
            "Srinagar",
            "Tehri"
        ]
        # City.objects.all().delete()
        # print('All cities are deleted')
        index = 0
        while index < len(cities):
            city_obj = City()
            city_obj.country_id = country
            city_obj.state_id = state
            city_obj.city = cities[index]
            city_obj.save()
            index += 1
        print('Successfully created cities.')
