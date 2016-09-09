# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from financeiro.views import *


urlpatterns = [
    #Url sucess
    url(r'^success/$',  SuccessView.as_view(), name='success'),

    #Urls relacionadas às views de Financeiro

    url(r'^pagamentos/resumo$',  PagamentoResumo.as_view(), name='pagamento_resumo'),
    #url(r'^pagamentos/detalhes/(?P<financeiro_id>\d+)/', financeiroDetalhesView.as_view(), name = 'financeiro_detalhes'),
    #url(r'^pagamentos/detalhes/editar/(?P<pk>\d+)/',financeiroEditar.as_view(),  name = 'financeiro_editar'),
    #url(r'^pagamentos/detalhes/deletar/(?P<pk>\d+)/',financeiroDeletar.as_view(),  name = 'financeiro_deletar'),
    url(r'^pagamentos/cadastro$', NotaFormView.as_view(), name = 'nota_cadastro'),
    url(r'^pagamentos/debitos$', DebitosListView.as_view(), name = 'financeiro_debitos'),
    url(r'^pagamentos/recebidos$', RecebidosListView.as_view(), name = 'financeiro_recebidos'),

    #Urls relacionadas às views de Estoque

    url(r'^estoque/resumo$',  EstoqueResumo.as_view(), name='estoque_resumo'),
    url(r'^estoque/cadastro$', ItemNotaFormView.as_view(), name = 'item_cadastro'),    
]
