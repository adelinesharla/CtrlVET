# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url

"""Classes de views genericas utilizadas"""
from django.views.generic import View, CreateView, TemplateView, DetailView, UpdateView, DeleteView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin

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

from django.forms.formsets import formset_factory

'Importacao para gerar pdf'
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from django.http import HttpResponse



class SuccessView(TemplateView):
	template_name='financeiro/success.html'	


class ProdutoFormView(FormView):
	pass

class ServicoFormView(FormView):
	pass


class PrestacaoContasView(TemplateView):
	template_name='financeiro/pagamento_pretacaocontas.html'	

class DebitoCreateView(CreateView):
	form_class = DebitoModelForm
	template_name = 'financeiro/debito_form.html'
	success_url = '/success/'

	def get_context_data(self, *args, **kwargs):
		context = super(DebitoCreateView, self).get_context_data(*args, **kwargs)
		context['debito_form'] = formset_factory(ProdutoModelForm)
		return context 

class DebitoFormView(FormView):
	template_name = 'financeiro/debito_form.html'
	form_class = DebitoModelForm
	success_url = '/success/'
	debito_formset = formset_factory(NotaModelForm)

	def form_valid(self, form):
		form.save()
		debito_formset.save()
		return HttpResponseRedirect('/success/')

	def get_context_data(self, *args, **kwargs):
		context = super(DebitoFormView, self).get_context_data(*args, **kwargs)
		context['debito_formset'] = formset_factory(NotaModelForm)
		return context 


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

class AnoList(ListView):
	model=Ano

class AnoDetalhesView(DetailView):
	pk_url_kwarg = "ano_id"
	model = Ano

	def get_context_data(self, **kwargs):
		context = super (AnoDetalhesView, self).get_context_data(**kwargs)

		debitos = self.object.debitos.all()
		soma = []
		for debito in debitos:
			soma.append(debito.itemNota.valor)
		context ['valor_total'] = sum(soma)
		soma = []
				
		for debito in debitos:
			if (debito.nota.setor == '1'):
				soma.append(debito.itemNota.valor)
		context ['pequenos'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '2'):
				soma.append(debito.itemNota.valor)
		context ['grandes'] = sum(soma)	
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '3'):
				soma.append(debito.itemNota.valor)
		context ['cirurgica'] = sum(soma)	
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '4'):
				soma.append(debito.itemNota.valor)
		context ['clinica'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '5'):
				soma.append(debito.itemNota.valor)
		context ['imagem'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '6'):
				soma.append(debito.itemNota.valor)
		context ['parasitologia'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '7'):
				soma.append(debito.itemNota.valor)
		context ['microbiologia'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '8'):
				soma.append(debito.itemNota.valor)
		context ['animal'] = sum(soma)
		soma = []

		return context

class GeraPdfPrestacaoContas(DetailView):
	model=Ano

	def get(self, request,ano):
		pk_url_kwarg = "ano_id"
		model = Ano
	
		response = HttpResponse(content_type='application/pdf')
		x =str(ano)
		response['Content-Disposition'] = 'attachment; filename= "Prestacao de contas.pdf"'
		pdf = canvas.Canvas(response)
		pdf.setLineWidth(.2)
		pdf.setFont('Helvetica', 12, leading=None)
		
		pdf.setFont('Helvetica', 16, leading=None)
		pdf.drawString(30,800,'Prestação de Contas''(Jan - Dez)')
		pdf.drawString(265,800,ano)
		pdf.setFont('Helvetica', 14, leading=None)
		
		coluna = 30
		colunaP = 440
		linha = 750
		espacamento = 35
		
		pdf.drawString(coluna,linha,'Setor')
		pdf.drawString(400,linha,'Valor Arrecadado (R$)')
		pdf.line(coluna,739,540,739)
		pdf.setFont('Helvetica', 12, leading=None)
		debitos = Debito.objects.all()
		linha = linha-espacamento
		soma = []
		
		for debito in debitos:
			if (debito.nota.setor == '1' and debito.ano.ano == ano):
				soma.append(debito.itemNota.valor)
		pdf.drawString(coluna,linha,'Clínica de Pequenos')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		
		soma = []
		linha = linha-espacamento
		
		for debito in debitos:
			if (debito.nota.setor == '2'and debito.ano.ano == ano):
				soma.append(debito.itemNota.valor)
		pdf.drawString(coluna,linha,'Clínica de Grandes')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		
		soma = []
		linha = linha-espacamento
		
		for debito in debitos:
			if (debito.nota.setor == '3'and debito.ano.ano == ano):
				soma.append(debito.itemNota.valor)
		pdf.drawString(coluna,linha,'Clínica Cirúrgica')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))	
			
		soma = []
		linha = linha-espacamento
		
		for debito in debitos:
			if (debito.nota.setor == '4'and debito.ano.ano == ano):
				soma.append(debito.itemNota.valor)
		pdf.drawString(coluna,linha,'Patologia Clínica')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))	
		
		soma = []
		linha = linha-espacamento
		
		for debito in debitos:
			if (debito.nota.setor == '5'and debito.ano.ano == ano):
				soma.append(debito.itemNota.valor)
		pdf.drawString(coluna,linha,'Diagnóstico por Imagem')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))	
		
		soma = []
		linha = linha-espacamento
		
		for debito in debitos:
			if (debito.nota.setor == '6'and debito.ano.ano == ano):
				soma.append(debito.itemNota.valor)
		pdf.drawString(coluna,linha,'Parasitologia')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
			
		soma = []
		linha = linha-espacamento
		
		for debito in debitos:
			if (debito.nota.setor == '7'and debito.ano.ano == ano):
				soma.append(debito.itemNota.valor)
		pdf.drawString(coluna,linha,'Microbiologia')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		
		soma = []
		linha = linha-espacamento
		
		for debito in debitos:
			if (debito.nota.setor == '8'and debito.ano.ano == ano):
				soma.append(debito.itemNota.valor)
		pdf.drawString(coluna,linha,'Patologia Animal')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		
		soma = []
		linha = linha-espacamento
		
		pdf.line(30,459,540,459)
		
		for debito in debitos:
			if debito.ano.ano == ano:
				soma.append(debito.itemNota.valor)
		pdf.drawString(coluna,linha,'Valor Total Arrecadado (R$)')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		
		soma = []
		linha = linha-espacamento
		pdf.showPage()
		pdf.save()
		return response


class EstoqueResumo(TemplateView):
	template_name='financeiro/estoque_resumo.html'

class ItemNotaFormView(FormView):
	template_name = 'financeiro/nota_form.html'
	form_class = ItemNotaModelForm
	success_url = '/success/'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')

class EfetuarPagamento(UpdateView):
	form_class = DebitoModelForm
	model = Debito
	success_url = '/pagamentos/resumo'
	def form_valid(self, form):
		
		form.save()
		return success_url
	
