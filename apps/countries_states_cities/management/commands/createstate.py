from django.core.management.base import BaseCommand

from apps.countries_states_cities.models import State


class Command(BaseCommand):
    help = "Enter the state details"

    @staticmethod
    def handle(*args, **options):
        print("Creating States...")
        country = 1
        states = ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh",
                  "Chhattisgarh", "Dadra and Nagar Haveli", "Daman and Diu", "Delhi", "Goa", "Gujarat", "Haryana",
                  "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Lakshadweep",
                  "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Orissa",
                  "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
                  "Uttarakhand", "West Bengal"]
        State.objects.all().delete()
        print('All states are deleted')
        index = 0
        while index < len(states):
            state_obj = State()
            state_obj.country_id = country
            state_obj.state = states[index]
            state_obj.save()
            index += 1
        print('Successfully created states.')
