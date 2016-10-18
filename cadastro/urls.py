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

    #Url sucess
    url(r'^success/$',  SuccessView.as_view(), name='success'),

    #Urls relacionadas às views de Tutor
    
    url(r'^tutor/resumo$',  TutorResumo.as_view(), name='tutor_resumo'),
    url(r'^tutor/detalhes/(?P<pk>\d+)/', TutorDetalhesView.as_view(), name = 'tutor_detalhes'),
    url(r'^tutor/detalhes/editar/(?P<pk>\d+)/',TutorEditar.as_view(),  name = 'tutor_editar'),
    url(r'^tutor/detalhes/deletar/(?P<pk>\d+)/',TutorDeletar.as_view(),  name = 'tutor_deletar'),
    url(r'^tutor/cadastro$', TutorFormView.as_view(), name = 'tutor_cadastro'),
    url(r'^tutor/busca$', TutorBuscaListView.as_view(), name = 'tutor_busca_list_view'),
    #url(r'^tutor/busca/avancada$', form_avancado, name = 'tutor_busca_avancada'),
    #url(r'^tutor/busca/avancada$', TutorBuscaAvancadaMixin.as_view(), name = 'tutor_busca_avancada'),
	 #url(r'^tutor/busca/avancada$', TutorBuscaAvancadaSingle.as_view(), name = 'tutor_busca_avancada'),
    #Urls relacionadas às views de Animal
    
      #Urls relacionadas às views de Animal
    url(r'^animal/resumo$',  AnimalResumo.as_view(), name='animal_resumo'),
    url(r'^animal/detalhes/(?P<pk>\d+)/', AnimalDetalhesView.as_view(), name = 'animal_detalhes'),
    url(r'^animal/detalhes/editar/(?P<pk>\d+)/',AnimalEditar.as_view(),  name = 'animal_editar'),
    url(r'^animal/detalhes/obito/(?P<pk>\d+)/',AnimalObito.as_view(),  name = 'animal_obito'),
    url(r'^animal/detalhes/deletar/(?P<pk>\d+)/',AnimalDeletar.as_view(),  name = 'animal_deletar'),
    url(r'^animal/cadastro$', AnimalFormView.as_view(), name = 'animal_cadastro'),
    url(r'^animal/busca$', AnimalBuscaListView.as_view(), name = 'animal_busca_list_view'),

    #url(r'^animal/busca/avancada$', AnimalBuscaAvancadaMixin.as_view(), name = 'animal_busca_avancada'),

    #Urls relacionadas às views de Consulta
    
    url(r'^consulta/cadastro$', ConsultaFormView.as_view(), name = 'consulta_cadastro'),
    url(r'^consulta/detalhes/deletar/(?P<pk>\d+)/',ConsultaDeleteView.as_view(),  name = 'consulta_deletar'),
    url(r'^consulta/detalhes/(?P<consulta_id>\d+)/', ConsultaDetailView.as_view(), name = 'consulta_detalhes'),
    url(r'^consulta/detalhes/editar/(?P<pk>\d+)/',ConsultaUpdateView.as_view(),  name = 'consulta_editar'),
    url(r'^consulta/$',ConsultaListView.as_view(), name='consulta_list'),
    url(r'^consulta/resumo$',ConsultaResumo.as_view(), name='consulta_resumo'),
    url(r'^consulta/busca$', ConsultaBuscaListView.as_view(), name = 'consulta_busca_list_view'),
    url(r'^consulta/busca/avancada$', ConsultaBuscaAvancadaMixin.as_view(), name = 'consulta_busca_avancada'),
    
    #Urls relacionadas às views de Exame
    
    url(r'^exames/$',LaboratorioResumo.as_view(), name='laboratorio_resumo'),
    url(r'^exames/laboratorio/detalhes/(?P<laboratorio_id>\d+)/$',LaboratorioDetailView.as_view(), name = 'laboratorio_detalhes'),
    url(r'^exames/laboratorio/(?P<pk>\d+)/cadastro/', ExameFormView.as_view(), name = 'exame_cadastro'),
    url(r'^exames/detalhes/deletar/(?P<pk>\d+)/$',ExameDeleteView.as_view(),  name = 'exame_deletar'),
    url(r'^exames/detalhes/(?P<pk>\d+)/',ExameDetailView.as_view(), name = 'exame_detalhes'),
    url(r'^exames/detalhes/editar/(?P<pk>\d+)/',ExameUpdateView.as_view(),  name = 'exame_editar'),
    
    url(r'^exame/$',ExameListView.as_view(), name='exame_list'),
    #url(r'^exame/resumo$',ExameResumo.as_view(), name='exame_resumo'),
    url(r'^exames/busca$', ExameBuscaListView.as_view(), name = 'exame_busca_list_view'),

    #exame/
    #exame/laboratorio/pk/exames
    #exame/laboratorio/pk/cadastro
    #exame/laboratorio/pk/exame/pk/detalhes
    #exame/laboratorio/pk/exame/pk/editar
    #

    ]
