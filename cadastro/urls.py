# _*_ coding: utf-8 _*_
"""cadastro URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from cadastro.views import *


urlpatterns = [
    url(r'^main/$|^$',  MainView.as_view(), name='main'),
    url(r'^tutor/resumo$',  TutorResumo.as_view(), name='tutor_resumo'),
    url(r'^animal/resumo$',  AnimalResumo.as_view(), name='animal_resumo'),
    url(r'^animal/detalhes/(?P<animal_id>\d+)/$', AnimalDetalhesView.as_view(), name = 'animal_detalhes'),
    url(r'^tutor/detalhes/(?P<tutor_id>\d+)/$', TutorDetalhesView.as_view(), name = 'tutor_detalhes'),
    url(r'(?P<pk>\d+)/$',TutorEditar.as_view(),  name = 'tutor_editar'),
    url(r'^tutor/cadastro$', TutorFormView.as_view(), name = 'tutor_cadastro'),
    url(r'^animal/cadastro$', AnimalFormView.as_view(), name = 'animal_cadastro'),
    url(r'^tutor/busca$', TutorBuscaListView.as_view(), name = 'tutor_busca_list_view'),
    url(r'^animal/busca$', AnimalBuscaListView.as_view(), name = 'animal_busca_list_view'),
    #url(r'^consulta/detalhes/(?P<consulta_id>\d+)/$', ConsultarDetalhesView.as_view(), name = 'consulta_detalhes'),
    #url(r'(?P<pk>\d+)/$',ConsultaEditar.as_view(),  name = 'consulta_editar'),
    #url(r'^exame/detalhes/(?P<exame_id>\d+)/$', ExaminarDetalhesView.as_view(), name = 'exame_detalhes'),
    #url(r'(?P<pk>\d+)/$',ExameEditar.as_view(),  name = 'exame_editar'),
    #url(r'^tutor/$',ListTutor.as_view(), name='tutor'),
    #url(r'^animal/$',ListAnimal.as_view(), name='animal'),
    #url(r'^consulta/$',ListConsulta.as_view(), name='consulta'),
    #url(r'^exame/$',ListExame.as_view(), name='exame'),
]
