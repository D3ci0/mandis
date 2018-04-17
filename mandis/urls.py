"""mandis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mandis.controllers import diagnosi_controller, sorgente_controller,\
    patologia_controller

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^diagnosi/$', diagnosi_controller.diagnosi_list),
    url(r'^sorgenti/$', sorgente_controller.sorgenti_list),
    url(r'^patologie/$', patologia_controller.patologie_list),
    url(r'^ricerca_sorgenti_per_diagnosi/$', sorgente_controller.sorgenti_per_diagnosi),
    url(r'^ricerca_malattie_per_area/$', diagnosi_controller.diagnosi_per_area),
    url(r'^ricerca_sorgenti_per_area/$', sorgente_controller.sorgenti_per_area),
    url(r'^ricerca_diagnosi_per_sorgente/$', diagnosi_controller.diagnosi_per_sorgente),
    url(r'^inserisci_sorgente/$', sorgente_controller.inserisci_sorgente),
]
