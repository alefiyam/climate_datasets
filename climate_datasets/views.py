from django.shortcuts import render, redirect
from models import *
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


def datasets(request):
    if 'country' in request.GET:
        # It will list data by country name
        country_name = request.GET['country']
        country = Country.objects.get(country_name=country_name)
    else:
        country = Country.objects.get(country_name='UK')
    temperature_ids = country.temperaturetype_set.values_list('id', flat=True)
    data = TemperatureData.objects.filter(temp_type__in=temperature_ids)
    countries = Country.objects.all()
    return render(request, 'home.html', {'country': countries, 'data': data})
