"""Country_State_City URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from apps.countries_states_cities.views import CountryListView, StateListView, CityListView

urlpatterns = [
    path('admin/', admin.site.urls),

    # """List Countries            : api/countries/""",
    # """Method: GET """,
    url(r'^api/countries/$', CountryListView.as_view(), name='countries'),
    # """List States            : api/states/id:country id""",
    # """Method: GET """,       """,
    url(r'^api/countries/(?P<id>[0-9]+)/states/$', StateListView.as_view(), name='state'),
    # """List Cities            : api/cities/id:state id""",
    # """Method: GET """,       """,
    url(r'^api/states/(?P<id>[0-9]+)/cities/$', CityListView.as_view(), name='city'),
]
