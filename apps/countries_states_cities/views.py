from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.
from apps.countries_states_cities.models import Country, State, City
from apps.countries_states_cities.serializer import CountrySerializer, StateSerializer, CitySerializer


class CountryListView(generics.ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class StateListView(generics.ListAPIView):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    def list(self, request, *args, **kwargs):
        country_id = self.kwargs['id']
        country = get_object_or_404(Country, id=country_id)
        state = State.objects.filter(country_id=country.id)
        ser = StateSerializer(state, many=True).data
        return Response(ser, status=status.HTTP_200_OK)


class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = State.objects.all()

    def list(self, request, *args, **kwargs):
        state_id = self.kwargs['id']
        state = get_object_or_404(State, id=state_id)
        city = City.objects.filter(state_id=state.id)
        ser = CitySerializer(city, many=True).data
        return Response(ser, status=status.HTTP_200_OK)
