
"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from pages import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^IncubatorProgramming/$', views.programmingPage, name='IncubatorProgramming'),
    url(r'^IncubatorSettingsPage/$', views.settingsPage, name='IncubatorSettingsPage'),
    url(r'^IncubatorHelpPage/$', views.helpPage, name='IncubatorHelpPage'),
    url(r'^IncubatorTemperature/$', views.temperatureView, name='IncubatorTemperature'),
    url(r'^IncubatorHumidity/$', views.humidityView, name='IncubatorHumidity'),

]
