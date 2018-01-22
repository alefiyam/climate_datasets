"""climate_datasets URL Configuration

"""

from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
import views

urlpatterns = [
    url(r'^datasets/$', views.datasets, name='datasets'),
    url(r'^admin/', admin.site.urls),
]
