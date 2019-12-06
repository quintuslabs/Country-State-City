from django.db import models


# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class State(models.Model):
    country = models.ForeignKey(Country, blank=False, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.state


class City(models.Model):
    country = models.ForeignKey(Country, blank=False, on_delete=models.CASCADE, primary_key=False)
    state = models.ForeignKey(State, blank=False, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.city
