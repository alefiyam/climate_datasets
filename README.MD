This application is made to show temperature for various regions yearwise.

Configuration Details :

To configure this appliction into your local machine you must have installed python 
and pip package of python.

Once you have installed above requirements then follow these instruction to configure this application.

clone/download this application repository into your local machine.
then navigate to climate_datasets directory and execute the following commands


In climate_datasets directory , execute the command :
$ pip install -r requirements.txt

This will install all require application dependencies.
As we used the Sqlite database and this database copy already exist in this application so you dont need to do any action with database. 


To get and save the climate data for various regions yearly execute the command :
    $ python manage.py climate_datasets.py
    
    This command is written to scrap the climate data from metoffice website
    and then parsed the html and then find the climate data for UK, England, 
    Wales and Scotland countries.

    This script is crawling Max Temp, Min Temp, Mean Temp, Shunshine and 
    Rainfall tables data then saving these data into django models.
    

To start this application just run the following command

    $ python manage.py runserver

This will start the Django server, you can access the applicaiton on your browser using this url.

	http://localhost:8000/datasets/

This will show the UK's(default) max , min , mean, rainfall , sunshine for all the months in various years. 


Following actions should be done:

1. To see the temperature of different countries, select the country from the countries dropdown ,    
   You can also search data by year , and temperature type.

2. To see the total number of records , select the number from dropdown.