
##########################################################################
#   This command script is to scrap climate data from 3rd party URL and parse
#   data then saved into the database.
#   URI = https://www.metoffice.gov.uk/climate/uk/summaries/datasets#yearOrdered
##########################################################################

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import re
import itertools
from operator import itemgetter
from django.apps import apps

# get_model method we used to import the models into Django Command.
Country = apps.get_model(app_label='climate_datasets', model_name='Country')
TemperatureType = apps.get_model(
    app_label='climate_datasets', model_name='TemperatureType')
TemperatureData = apps.get_model(
    app_label='climate_datasets', model_name='TemperatureData')


class Command(BaseCommand):
    '''
    This command is written to scrap the climate data from metoffice website
    and then parsed the html and then find the climate data for UK, England, 
    Wales and Scotland countries.

    this script is crawliing Max Temp, Min Temp, Mean Temp, Shunshine and 
    Rainfall tables data then saving these data into django models.
    '''

    help = 'Get Climate DataSets'

    def add_argument(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            url = 'https://www.metoffice.gov.uk/climate/uk/summaries/datasets#yearOrdered'
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')

            yearly_statistics = soup.find(
                "table", {"summary": "Year ordered statistics"})

            # find required countries rows from HTML using HTML parser.
            countries_tr = yearly_statistics.find_all('tr')[1:5]

            country_data_list = []
            country_dict = {}

            # iterating each countries to scrap specific temperature type data.
            for index, country in enumerate(countries_tr):
                print(" Please wait while data is getting saved ...")

                # saving the country name into django Country Models, if
                # Country name already exist then it will return the country
                # object.
                country_obj, temp1 = Country.objects.get_or_create(
                    country_name=country.find('strong').text)

                # find required (Max Temp, Min Temp, Mean Temp, Shunshine and
                # Rainfall) columns from HTML
                uk_max_temp = country.find_all('a', href=True)[0:5]

                # iterating each coulumn then also performing a GET request to
                # fetch the climate data of a specific temperature type.
                for temp in uk_max_temp:
                    month_temp_dict = {}
                    list_of_dict = []
                    temp_type = str(temp['href'].split(
                        'datasets/')[1].split('/ranked')[0])

                    # saving the temerature type into django TemperatureType
                    # Models, if specific TemperatureType already exist then it
                    # will return the TemperatureType object.
                    temp_type_obj, temp2 = TemperatureType.objects. \
                        get_or_create(temprature_type=temp_type,
                                      country=country_obj
                                      )

                    # performing GET request to get the specific temperature
                    # type detailed data.
                    page = requests.get(temp['href'])

                    content = page.content.split('\r\n')
                    month = content[7]
                    month = re.sub('[ \t]+', ' ', month).split()

                    # iterating the temperature data and create data sets in a
                    # formate that can be saved into Django model.
                    for temperature in content[8:]:
                        temperature = re.sub(
                            '[ \t]+', ' ', temperature).split()
                        for m, t in zip(month, temperature):
                            if m == 'Year':
                                month_temp_dict[m] = t
                                list_of_dict.append(month_temp_dict)
                                month_temp_dict = {}
                                continue
                            else:
                                month_temp_dict[m] = t

                    list_of_dict = sorted(list_of_dict, key=itemgetter('Year'))

                    for key, value in itertools.groupby(
                        list_of_dict,
                        key=itemgetter('Year')
                    ):
                        result = {}
                        for i in value:
                            result.update(i)

                        # updating temperature type in the result disctionary
                        # object, so TemperatureType models can be assosiated
                        # with TemperatureData Model.
                        result['temp_type'] = temp_type_obj

                        # saving the result dictionary object into the Django
                        # TemperatureData Model.
                        temp_data_obj, temp3 = TemperatureData.objects. \
                            update_or_create(**result)

            print(" Data saved into the database successfully !")
        except Exception as e:
            print(e)
