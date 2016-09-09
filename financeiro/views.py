# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url

"""Classes de views genericas utilizadas"""
from django.views.generic import View, FormView, TemplateView, DetailView, UpdateView, DeleteView, ListView, FormView

'HttpResponse para uma pagina template indicando que a operação foi realizada (verificar se tal página existe)'
from django.http import HttpResponseRedirect

'Importando Formularios necessários para views de tutor e animal'
from .forms import *
'Importando Models necessárias para views de tutor e animal'
from .models import *

from django.forms.models import model_to_dict #iterar em object no template

'Importando atributos da model a serem utilizados nas buscas'
import operator
from django.db.models import Q


class SuccessView(TemplateView):
	template_name='financeiro/success.html'	


class ProdutoFormView(FormView):
	pass

class ServicoFormView(FormView):
	pass

class NotaFormView(FormView):
	template_name = 'financeiro/nota_form.html'
	form_class = ItemNotaModelForm
	success_url = '/success/'

	def form_valid(self, faorm):
		form.save()
		return HttpResponseRedirect('/success/')

class DebitosList(ListView):
	model = Debito
	paginate_by = 10

class DebitosListView(DebitosList):
	template_name = 'financeiro/debitos_list.html'
	def get_queryset(self):
		return Debito.objects.filter(status=0)

class RecebidosListView(DebitosList):
	template_name = 'financeiro/recebidos_list.html'
	def get_queryset(self):
		return Debito.objects.filter(status=1)

class PagamentoResumo(TemplateView):
	template_name='financeiro/pagamento_resumo.html'
	
	def get_context_data(self, *args, **kwargs):
		context = super(PagamentoResumo, self).get_context_data(*args, **kwargs)
		context['recebidos_list'] = Debito.objects.filter(status=1).order_by('status')[:5]
		context['debitos_list'] = Debito.objects.filter(status=0).order_by('status')[:5]
		return context 


'''class ListPagamento(ListView):
	model = GENERIC_PAGAMENTO
	paginate_by = 10

class EfetuarPagamento(FormView):
	template_name = 'financeiro/GENERICO_PAGAMENTO_FORM.HTML'
	form_class = GENERIC_PAG_FORM
	success_url = '/success/'
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')
  
class AlterarPagamento(UpdateView):
	form_class = GENERIC_PAG_FORM
	model = GENERIC_PAGAMENTO
	fields = '_all_'
	template_name_suffix = '_update_form'
	success_url = '/success/'

class CancelarPagamento(self):
	model = GENERIC_PAGAMENTO
	success_url = reverse_lazy('tutor_resumo')
	success_url = '/successs/'
  
class DetalhesPagamento(DetailView):
	pk_url_kwarg = "generic_id"
	model = GENERIC_PAGAMENTO

	def get_context_data(self, **kwargs):
		context = super(DetalhesPagamento, self).get_context_data(**kwargs)
		return context
	  
class PagamentoBuscaListView(self):
  def get_queryset(self):
	result = super(PagamentoBuscaListView, self).get_queryset()
	query = self.request.GET.get('q')
	if query:
		query_list = query.split()
		result = result.filter(
		reduce(operator.and_,
		(Q(_nome__icontains=q) for q in query_list)) |
		reduce(operator.and_,
		(Q(_email__icontains=q) for q in query_list)) |
		reduce(operator.and_,
		(Q(_cpf__icontains=q) for q in query_list))
		)

		return result'''



class EstoqueResumo(TemplateView):
	template_name='financeiro/estoque_resumo.html'

class ItemNotaFormView(FormView):
	template_name = 'financeiro/nota_form.html'
	form_class = ItemNotaModelForm
	success_url = '/success/'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')
